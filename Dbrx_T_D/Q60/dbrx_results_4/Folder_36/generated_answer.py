from sympy import isprime

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 10:
        n = int(str(n)[1:])
        if not isprime(n):
            return False
    return isprime(n)

def all_left_right_truncatable_prime(t):
    x = t[992]
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)