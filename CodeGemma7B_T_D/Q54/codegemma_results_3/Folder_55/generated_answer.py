from sympy import isprime

def all_right_truncatable_prime(x):
    l = []
    for i in range(2, int(x / 2)):
        if isprime(i):
            a = str(i)
            b = a[:-1]
            while len(b) > 0 and int(b) in range(2, int(x / 2)):
                if isprime(int(b)):
                    l.append(i)
                b = b[:-1]
    if len(l) == 0:
        return []
    return sorted(l, reverse=True)