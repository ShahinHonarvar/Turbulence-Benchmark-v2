from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[25]
    r = sorted([i for i in range(2, x) if isprime(i) and all((isprime(int(str(i)[:-j])) for j in range(1, len(str(i)))))], reverse=True)
    return r or []