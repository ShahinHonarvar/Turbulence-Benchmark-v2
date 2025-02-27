from math import sqrt

def all_left_right_truncatable_prime(t):
    x = t[370]
    res = []
    for a in range(2, x + 1):
        b = str(a)
        if not '0' in b:
            l = int(b)
            r = int(b[::-1])
            if is_prime(l) and is_prime(r):
                res.append(a)
    res.sort(reverse=True)
    return res

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    up_limit = int(sqrt(n)) + 1
    for divisor in range(2, up_limit):
        if n % divisor == 0:
            return False
    return True