import sympy

def is_left_truncatable_prime(n):
    if n <= 0:
        return False
    if n % 10 == 0 or sympy.isprime(n) is False:
        return False
    i = 10
    while i <= n:
        if sympy.isprime(n // i) == False:
            return False
        i *= 10
    return True

def all_left_truncatable_prime(u):
    x = u[70]
    result = []
    for n in range(2, x):
        if is_left_truncatable_prime(n):
            result.append(n)
    return sorted(result)