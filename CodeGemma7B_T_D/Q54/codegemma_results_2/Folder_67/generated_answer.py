from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable(n):
    if not is_prime(n):
        return False
    div = 10
    while n // div:
        p = n // div
        if not is_prime(p):
            return False
        n = p
        div *= 10
    return True

def all_right_truncatable_prime(tu):
    x = tu[71]
    res = []
    for n in range(x - 1, 0, -1):
        if right_truncatable(n):
            res.append(n)
    return sorted(res, reverse=True)