import sympy

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        while n > 0:
            if not sympy.isprime(n):
                return False
            n //= 10
        return True
    x = numbers[0] if len(numbers) == 1 else numbers[1]
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(right_truncatable_primes, reverse=True)