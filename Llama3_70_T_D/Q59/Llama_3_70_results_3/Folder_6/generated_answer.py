import sympy

def is_left_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        if not sympy.isprime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[74]
    truncatable_primes = [i for i in range(1, x) if is_left_truncatable_prime(i) and sympy.isprime(i)]
    return sorted(truncatable_primes)