import sympy

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        if not sympy.isprime(n):
            return False
        while n > 0:
            n //= 10
            if n > 0 and (not sympy.isprime(n)):
                return False
        return True
    x = numbers[24]
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(right_truncatable_primes)