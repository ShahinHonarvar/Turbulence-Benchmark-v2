from math import sqrt

def all_left_right_truncatable_prime(tup):
    x = tup[433]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        if is_prime(i):
            str_i = str(i)
            if '0' not in str_i:
                left_trunc = int(str_i[1:])
                right_trunc = int(str_i[:-1])
                if is_prime(left_trunc) and is_prime(right_trunc):
                    primes.append(i)
    primes.sort(reverse=True)
    return primes