import sympy

def is_left_truncatable_prime(n):
    if n < 10:
        return sympy.isprime(n)
    if n % 10 == 0:
        return False
    if not sympy.isprime(n):
        return False
    return is_left_truncatable_prime(n // 10)

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[96]
    return sorted([n for n in sympy.primerange(2, x) if is_left_truncatable_prime(n)], reverse=True)