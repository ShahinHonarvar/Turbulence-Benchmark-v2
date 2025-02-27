from sympy import isprime

def all_left_right_truncatable_prime(ns):

    def is_left_right_truncatable_prime(n):
        if not (str(n).isdigit() and isprime(n) and ('0' not in str(n))):
            return False
        digits = len(str(n))
        for i in range(1, digits):
            if not isprime(int(str(n)[:i])) or not isprime(int(str(n)[i:])):
                return False
        return True
    x = ns[175]
    return sorted((n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)))