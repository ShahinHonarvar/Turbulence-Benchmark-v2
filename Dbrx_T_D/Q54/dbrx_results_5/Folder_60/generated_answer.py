from sympy import isprime

def is_right_truncatable_prime(n):
    while n > 0:
        if not isprime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_right_truncatable_prime(t):
    x = t[87]
    result = []
    for num in range(1, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)