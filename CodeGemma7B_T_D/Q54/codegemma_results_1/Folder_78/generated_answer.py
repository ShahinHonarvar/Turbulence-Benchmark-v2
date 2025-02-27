from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[23]
    res = []
    for i in range(2, x):
        if isprime(i):
            temp = i
            while temp:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                res.append(i)
    res.sort()
    return res if res else []