from sympy import isprime

def all_left_truncatable_prime(a):
    x = a[73]
    res = []
    for i in range(10 ** (len(str(x)) - 1), x):
        if isprime(i):
            s = str(i)
            for j in range(1, len(s)):
                if not isprime(int(s[j:])):
                    break
            else:
                res.append(i)
    return sorted(res, reverse=True)