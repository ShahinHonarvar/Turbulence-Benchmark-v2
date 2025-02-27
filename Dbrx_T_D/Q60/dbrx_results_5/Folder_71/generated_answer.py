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
    if not is_truncatable_prime(int(str(n)[1:])):
        return False
    if not is_truncatable_prime(int(str(n)[:-1])):
        return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[22]
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncated = [int(str(i)[j:]) for j in range(len(str(i)))]
            truncated += [int(str(i)[:j]) for j in range(1, len(str(i)))]
            if all((is_prime(n) for n in truncated)):
                result.append(i)
    return sorted(result, reverse=True)