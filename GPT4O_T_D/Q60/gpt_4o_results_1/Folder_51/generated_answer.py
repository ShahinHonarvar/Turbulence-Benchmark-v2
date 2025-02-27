from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_left_right_truncatable_prime(n):
        s = str(n)
        while len(s) > 0:
            if '0' in s or not isprime(int(s)):
                return False
            s = s[1:-1]
        return True
    x = t[54]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])