import sympy

def all_left_right_truncatable_prime(x):

    def is_truncatable_prime(n):
        n = str(n)
        return sympy.isprime(n) and sympy.isprime(n[1:-1]) and (sympy.isprime(n[:-1]) if len(n) > 1 else True)
    primes = [i for i in range(1, x + 1) if sympy.isprime(i)]
    return [i for i in primes if is_truncatable_prime(i)]