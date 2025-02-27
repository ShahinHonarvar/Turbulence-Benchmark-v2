from math import isprime

def all_left_right_truncatable_prime(a):
    res = []
    for i in range(a[29] + 1):
        if str(i).find('0') >= 0:
            continue
        if isprime(i):
            l = list(str(i))
            while len(l) >= 2:
                l.pop(0)
                k = int(''.join(l))
                if not isprime(k):
                    break
                l.pop(-1)
                k = int(''.join(l))
                if not isprime(k):
                    break
            else:
                res.append(i)
    return sorted(res, reverse=True)