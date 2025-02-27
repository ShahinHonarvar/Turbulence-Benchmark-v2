from functools import lru_cache

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def is_left_and_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if n % 10 == 0 or not is_prime(n):
        return False
    return is_left_and_right_truncatable_prime(n // 10) and is_left_and_right_truncatable_prime(n % 10)

def all_left_right_truncatable_prime(t):
    x = t[43]
    return sorted(list(filter(is_left_and_right_truncatable_prime, range(1, x + 1)))) if x > 1 else []