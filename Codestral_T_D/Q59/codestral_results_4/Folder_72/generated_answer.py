import sympy

def all_left_truncatable_prime(t):
    x = t[31]

    def is_left_truncatable_prime(n):
        if sympy.isprime(n):
            while n > 9:
                n = int(str(n)[1:])
                if not sympy.isprime(n):
                    return False
            return True
        return False
    return sorted(filter(is_left_truncatable_prime, range(2, x)), reverse=True)