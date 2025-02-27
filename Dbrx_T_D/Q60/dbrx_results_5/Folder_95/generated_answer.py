from sympy import isprime

def truncatable_prime(n):
    if n < 10:
        return isprime(n)
    if not n % 10 or n % 10 == 5 or '0' in str(n):
        return False
    return truncatable_prime(int(str(n)[1:])) and truncatable_prime(int(str(n)[:-1]))

def all_left_right_truncatable_prime(t):
    x = t[77]
    return sorted([i for i in range(1, x + 1) if truncatable_prime(i)])