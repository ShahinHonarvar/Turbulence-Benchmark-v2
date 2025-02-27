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

def right_truncate(n):
    return int(str(n)[:-1])

@lru_cache(maxsize=None)
def is_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_right_truncatable_prime(right_truncate(n))

def all_left_right_truncatable_prime(t):
    x = list(t)[67]
    primes = [p for p in range(2, x + 1) if is_left_truncatable_prime(p) and is_right_truncatable_prime(p)]
    return sorted(list(set(primes)), reverse=True)