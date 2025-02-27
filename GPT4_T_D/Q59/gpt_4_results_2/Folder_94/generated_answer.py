import sympy as sp

def all_left_truncatable_prime(t):
    x = t[43]

    def is_left_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not sp.isprime(int(s[i:])):
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])