from sympy import isprime

def truncatable(n):
    while n > 0:
        if not isprime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_right_truncatable_prime(t):
    x = t[18]
    result = []
    for i in range(1, x):
        if isprime(i) and truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)