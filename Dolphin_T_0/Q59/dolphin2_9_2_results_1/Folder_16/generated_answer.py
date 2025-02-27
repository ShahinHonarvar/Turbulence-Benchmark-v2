import sympy

def is_left_truncatable_prime(n):
    for i in range(1, len(str(n))):
        if not sympy.isprime(int(str(n)[i:])):
            return False
    return sympy.isprime(n)

def all_left_truncatable_prime(numbers):
    x = numbers[792]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])