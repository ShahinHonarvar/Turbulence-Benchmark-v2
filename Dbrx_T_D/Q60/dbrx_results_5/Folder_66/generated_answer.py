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
    if not is_prime(n) or '0' in str(n):
        return False
    if n < 10:
        return True
    return is_left_and_right_truncatable_prime(int(str(n)[1:])) and is_left_and_right_truncatable_prime(int(str(n)[:-1]))

def all_left_right_truncatable_prime(tup):
    x = tup[25]
    return sorted([i for i in range(2, x + 1) if is_left_and_right_truncatable_prime(i)], reverse=True)