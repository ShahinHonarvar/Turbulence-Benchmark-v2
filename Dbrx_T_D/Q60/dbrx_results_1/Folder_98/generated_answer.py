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
    return is_prime(n) and (n < 10 or is_left_truncatable_prime(n // 10))

@lru_cache(maxsize=None)
def is_right_truncatable_prime(n):
    return is_prime(n) and (n < 10 or is_right_truncatable_prime(n % 10))

def all_left_right_truncatable_prime(args):
    x = args[8]
    result = []
    for num in range(1, x + 1):
        s = str(num)
        if '0' in s or len(s) < 2 or is_left_truncatable_prime(num) is False or (is_right_truncatable_prime(num) is False):
            continue
        for i in range(1, len(s)):
            if is_prime(int(s[i:])) is False or is_prime(int(s[:-i])) is False:
                break
        else:
            result.append(num)
    return sorted(result, reverse=True)