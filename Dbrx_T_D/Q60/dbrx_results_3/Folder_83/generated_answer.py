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
    if not is_prime(n):
        return False
    if n < 10:
        return True
    while n:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(n):
    return sorted((x for x in range(24, n + 1) if is_left_and_right_truncatable_prime(x)))