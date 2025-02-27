def all_right_truncatable_prime(t):
    x = t[28]
    result = []
    for i in range(2, x):
        if is_prime(i) and is_truncable(i):
            result.append(i)
    result.sort()
    return result if len(result) > 0 else []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncable(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:-i])):
            return False
    return True