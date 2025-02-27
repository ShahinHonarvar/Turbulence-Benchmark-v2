from sympy import isprime

def is_truncatable_prime(n):
    s = str(n)
    for i in range(1, len(s)):
        if not isprime(int(s[i:])) or not isprime(int(s[:i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    if len(t) <= 370:
        return []
    x = t[370]
    truncatable_primes = [n for n in range(10, x + 1) if isprime(n) and is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)