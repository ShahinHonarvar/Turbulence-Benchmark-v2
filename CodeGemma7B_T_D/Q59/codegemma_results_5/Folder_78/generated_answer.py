from sympy import isprime, nextprime

def all_left_truncatable_prime(a):
    b = a[23]
    c = []
    k = nextprime(b)
    while k < b:
        k = nextprime(k)
        l = str(k)
        m = int(''.join(l))
        if isprime(k) == True and '0' not in l and (len(l) > 1):
            for i in range(1, len(l)):
                n = int(''.join(l[i:]))
                if isprime(n) == False:
                    break
                if n == l[-1:]:
                    c.append(k)
    return sorted(c)