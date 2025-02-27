from sympy import isprime

def all_left_right_truncatable_prime(x):
    y = []
    x = int(x[77])
    for k in range(2, x):
        if isprime(k) and (not '0' in str(k)):
            l, r = (k, k)
            while l >= 10 and r >= 10:
                l = str(l)[1:]
                l = int(l)
                r = str(r)[:-1]
                r = int(r)
                if isprime(l) and isprime(r):
                    y.append(k)
    y.sort(reverse=True)
    return y