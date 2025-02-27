def all_left_right_truncatable_prime(t):
    x = t[11]
    res = []
    for i in range(2, x + 1):
        if is_prime(i):
            s = str(i)
            if '0' not in s:
                l, r = ([s] * (len(s) // 2), [s] * (len(s) // 2))
                ok = True
                while len(l) >= 1 and len(r) >= 1:
                    l, r = (l[:-1], r[1:])
                    if not is_prime(int(''.join(l))):
                        ok = False
                        break
                    if not is_prime(int(''.join(r))):
                        ok = False
                        break
                if ok:
                    res.append(i)
    return sorted(res)

def is_prime(p):
    if p == 1:
        return False
    if p in (2, 3):
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False
    i = 5
    while i * i <= p:
        if p % i == 0 or p % (i + 2) == 0:
            return False
        i += 6
    return True