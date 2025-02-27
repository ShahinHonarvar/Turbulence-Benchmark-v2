from sympy import factorint

def all_left_truncatable_prime(t):
    x = t[86]
    res = []
    for n in range(2, x):
        if factorint(n) == 1:
            a = list(str(n))
            if '0' in a or len(a) != len(set(a)):
                continue
            for m in a[1:]:
                if factorint(int(m)) != 1:
                    break
            else:
                res.append(n)
    return sorted(res)