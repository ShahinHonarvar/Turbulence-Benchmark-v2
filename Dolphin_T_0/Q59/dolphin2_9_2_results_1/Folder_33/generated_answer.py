import sympy

def all_left_truncatable_prime(integer_tuple):

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        while n > 1:
            if sympy.isprime(n):
                n //= 10
            else:
                return False
        return True
    x = integer_tuple[945]
    primes = [n for n in range(2, x) if sympy.isprime(n) and is_left_truncatable_prime(n)]
    return sorted(primes, reverse=True)