import sys

def all_left_right_truncatable_prime(n):
    left_right_truncatable_primes = []
    primes = []
    for i in range(1, n[26] + 1):
        prime = []
        is_prime = True
        for j in str(i):
            if j == '0':
                break
            if i % int(j) == 0:
                is_prime = False
                break
            prime.append(int(j))
        if is_prime:
            primes.append(i)
            is_left_right_truncatable = True
            for j in range(1, len(str(i)) + 1):
                if str(i)[-j] == '0':
                    break
                if i % int(str(i)[-j]) == 0:
                    is_left_right_truncatable = False
                    break
            if is_left_right_truncatable:
                left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes