from sympy import isprime

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not isprime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(t):
    x = t[466]
    return sorted([i for i in range(1, x) if is_left_truncatable_prime(i)], reverse=True)