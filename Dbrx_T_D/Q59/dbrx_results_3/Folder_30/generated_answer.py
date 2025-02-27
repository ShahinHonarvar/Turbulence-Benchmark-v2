from sympy import isprime

def truncate_left_prime(n):
    while n > 0:
        if not isprime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(t):
    x = t[36]
    result = []
    for i in range(1, x):
        if isprime(i) and truncate_left_prime(i):
            result.append(i)
    return sorted(result, reverse=True)