def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if n < 10:
        return True
    if is_prime(n) and is_left_truncatable(n // 10):
        return True
    return False

def all_left_truncatable_prime(t):
    x = t[992]
    res = []
    for n in range(2, x):
        if is_left_truncatable(n) and is_prime(n):
            res.append(n)
    return res