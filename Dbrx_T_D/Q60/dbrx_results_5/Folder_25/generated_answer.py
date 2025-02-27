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
    for i in range(10, 36, 2):
        if n % i == 0:
            return False
    return is_left_truncatable_prime(n // 10)

@lru_cache(maxsize=None)
def is_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    for i in range(10, 36, 2):
        if n % 10 ** i == 0:
            return False
    return is_right_truncatable_prime(n // 10)

def all_left_right_truncatable_prime(bound_tuple):
    x = 10005 if bound_tuple[92] > 10005 else bound_tuple[92]
    result = []
    for i in range(10, x + 1):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)