from math import *

def is_prime(n):
    if n <= 1:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n):
    k = int(log10(n))
    while k >= 0:
        p = int(n % int(10 ** (k + 1)))
        if not is_prime(p):
            return False
        n //= 10
        k -= 1
    return True

def all_right_truncatable_prime(tp):
    if not all([isinstance(a, int) for a in tp]):
        return []
    elif len(tp) <= 371:
        return []
    elif not is_prime(tp[-1]):
        return []
    else:
        z = list(set(tp))
        z.sort(reverse=True)
        size = len(z)
        arr = []
        if is_right_truncatable_prime(z[0]):
            arr = z[1:size]
            arr.sort(reverse=True)
        return arr