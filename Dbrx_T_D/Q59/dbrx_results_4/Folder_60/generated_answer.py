from sympy import isprime

def is_left_truncatable_prime(n):
    n = str(n)
    if len(n) == 1 and int(n) > 1:
        return True
    for i in range(1, len(n)):
        if not isprime(int(n[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[87]
    result = []
    for num in range(1, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)