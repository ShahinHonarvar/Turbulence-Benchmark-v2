from sympy import prime

def is_prime(n):
    return prime(n).is_prime

def left_truncatable(l, n):
    if l == n:
        return True
    if l % 10 == 0:
        return False
    if not is_prime(l):
        return False
    return left_truncatable(l // 10, n)

def right_truncatable(l, n):
    if n == 0:
        return True
    if l % 10 == 0:
        return False
    if not is_prime(l):
        return False
    return right_truncatable(l % 10, n - 1)

def all_left_right_truncatable_prime(t):
    d = list(map(int, str(t[429])))
    res = []
    for l in range(2, d[-1] + 1):
        if left_truncatable(l, d[-1]):
            if right_truncatable(l, d[-1]):
                res.append(l)
    res.sort(reverse=True)
    return res or []