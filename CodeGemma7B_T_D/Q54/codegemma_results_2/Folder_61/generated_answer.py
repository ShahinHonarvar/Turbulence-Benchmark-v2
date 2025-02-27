from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[3]
    for i in range(int(x ** 0.5) + 1):
        i += 2
        if isprime(i):
            f = i
            p = True
            while f > 0:
                if not isprime(f):
                    p = False
                    break
                f //= 10
            if p:
                yield i