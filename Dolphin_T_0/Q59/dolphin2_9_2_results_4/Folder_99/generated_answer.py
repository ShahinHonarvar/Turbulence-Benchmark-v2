from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[758]
    res = []
    for i in range(2, x):
        n = i
        while isprime(n):
            if n != i:
                break
            n //= 10
        if n == 0 and isprime(i):
            res.append(i)
    return sorted(res)