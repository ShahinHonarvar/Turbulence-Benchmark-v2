from itertools import count
  from functools import reduce

def all_left_right_truncatable_prime(n):

    def sieve(limit, bottom):
        C = {i for i in range(bottom, limit + 1)}
        c = 0
        l = list(C)
        while c < len(l):
            i = l[c]
            C -= {j for j in range(i + i, limit + 1, i)}
            c += 1
        return [i for i in C if i >= bottom]
    prime_til = n + 1
    primes = sieve(prime_til, 2)
    L = True
    while L:
        list_of_digits = [[int(x) for x in list(str(a))] for a in primes]
        for digit in list_of_digits:
            if 0 in digit:
                L = False
                continue
        if L:
            for digit in list_of_digits:
                cut_length = len(digit)
                for i in range(cut_length):
                    left = digit[i:]
                    right = digit[:len(digit) - i - 1:-1]
                    if left == list(str(int(''.join([str(a) for a in left])))) and right == list(str(int(''.join([str(a) for a in right])))) and (int(''.join([str(a) for a in left])) * int(''.join([str(a) for a in right])) > prime_til):
                        L = False
                        continue
            if L:
                list_of_primes = [int(''.join([str(a) for a in digit])) for digit in list_of_digits]
                return sorted(list_of_primes)
    if not L:
        return []