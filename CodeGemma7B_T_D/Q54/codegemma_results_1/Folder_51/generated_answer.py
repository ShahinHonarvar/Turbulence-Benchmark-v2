from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[54]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            while i % 10 != 0 and is_prime(i):
                i //= 10
            if i % 10 == 0:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)