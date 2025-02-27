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
    if not is_prime(n):
        return False
    return is_truncatable_prime(n // 10) and is_truncatable_prime(n % 10)

def all_left_right_truncatable_prime(t):
    x = t[3]
    result = []
    for num in range(10, x + 1):
        if is_truncatable_prime(num):
            is_left_truncatable = all((is_truncatable_prime(int(str(num)[i:])) for i in range(1, len(str(num)))))
            is_right_truncatable = all((is_truncatable_prime(int(str(num)[:-i])) for i in range(1, len(str(num)))))
            if is_left_truncatable and is_right_truncatable:
                result.append(num)
    return sorted(result, reverse=True)