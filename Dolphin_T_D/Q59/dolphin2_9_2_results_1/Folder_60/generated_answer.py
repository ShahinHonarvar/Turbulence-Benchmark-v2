from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[87]
    res = []
    for i in range(2, x):
        if isprime(i):
            n = i
            while n != 0:
                if not isprime(n):
                    break
                n //= 10
            else:
                res.append(i)
    return sorted(res)