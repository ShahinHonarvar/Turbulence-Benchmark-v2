import sympy

def all_left_right_truncatable_prime(t):
    x = t[77]

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        n = int(str_n)
        while n > 9:
            n = int(str_n[1:-1])
            str_n = str(n)
            if not sympy.isprime(n):
                return False
        return sympy.isprime(n)
    return [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]