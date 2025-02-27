from itertools import count, islice

def is_prime(n):
    n = abs(n)
    if n < 2:
        return False
    for i in islice(count(n - 1, -2), n // 2 + 1):
        if not n % i:
            return False
    return True

def is_normal(n):
    if '0' in str(n):
        return False
    while n > 9:
        n = int(str(n)[:-1])
        if not is_prime(n):
            return False
    return True

def left_truncatable_prime(p):
    p = str(p)
    for i in range(len(p)):
        n = int(p[i:])
        if not (is_prime(n) and is_normal(n)):
            return False
    return True

def right_truncatable_prime(p):
    p = str(p)
    for i in range(len(p)):
        n = int(p[:len(p) - i - 1])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[79]
    return sorted([i for i in range(x + 1) if left_truncatable_prime(i) and right_truncatable_prime(i)], reverse=True)