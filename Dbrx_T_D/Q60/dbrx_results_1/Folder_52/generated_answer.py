from functools import lru_cache

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def is_left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_left_truncatable_prime(n // 10)

@lru_cache(maxsize=None)
def is_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_right_truncatable_prime(n // 10)

def all_left_right_truncatable_prime(r):
    x = 7 if r[52] >= 7 else r[52]
    primes = []
    for i in range(1, 10):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    for i in range(10, x + 1):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)[::-1]