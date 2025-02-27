import sympy

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        if not sympy.isprime(n):
            return False
        n = str(n)
        while len(n) > 1:
            n = n[:-1]
            if not sympy.isprime(int(n)):
                return False
        return True
    if len(numbers) < 99:
        return []
    x = numbers[98]
    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes)