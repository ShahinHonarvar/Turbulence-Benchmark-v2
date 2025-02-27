from sympy import isprime

def left_truncate(n):
    return int(str(n)[1:])

def is_left_truncatable_prime(n):
    if '0' in str(n) or not isprime(n):
        return False
    while n > 10:
        n = left_truncate(n)
        if not isprime(n):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[71]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)