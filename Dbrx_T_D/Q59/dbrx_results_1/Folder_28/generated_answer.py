from functools import lru_cache

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and left_truncatable_prime(n % 10)

def all_left_truncatable_prime(t):
    x = t[19]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in primes if left_truncatable_prime(i)])