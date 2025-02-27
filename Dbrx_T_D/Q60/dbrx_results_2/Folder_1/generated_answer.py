from functools import lru_cache

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_truncatable_prime(int(str(n)[1:])) and is_truncatable_prime(int(str(n)[:-1]))

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[20]
    result = []
    for i in range(10, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)