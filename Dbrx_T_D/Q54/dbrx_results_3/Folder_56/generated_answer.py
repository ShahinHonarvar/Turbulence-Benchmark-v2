from sympy import isprime

def all_right_truncatable_prime(indices):
    x = 31

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    primes = [i for i in range(1, x) if is_right_truncatable_prime(i)]
    return sorted((prime for prime in primes if prime < x))