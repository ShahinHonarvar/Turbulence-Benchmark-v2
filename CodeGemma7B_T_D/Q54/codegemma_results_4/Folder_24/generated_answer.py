from math import sqrt
    from functools import cmp_to_key

def all_right_truncatable_prime(t):
    x = t[64]
    y = list(range(2, x))
    s, primer = ([], [])
    pos = -1
    while y and pos < len(y) - 1:
        pos += 1
        if all_right_truncatable_prime.is_prime(y[pos]) and all_right_truncatable_prime.is_prime(y[pos * pos, x] & y[pos]):
            primer.append(y[pos])
            if pos:
                s.append(y[pos])
    if not primer:
        return []
    return sorted(s, key=cmp_to_key(lambda a, b: b - a)) + sorted(primer, key=cmp_to_key(lambda a, b: b - a))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True