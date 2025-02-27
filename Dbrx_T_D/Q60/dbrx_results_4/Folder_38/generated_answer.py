from sympy import isprime

def all_left_right_truncatable_prime(limit_tuple):
    limit = limit_tuple[0]
    primes = [i for i in range(2, limit + 1) if isprime(i)]
    ltr_primes = []

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
        return True
    for prime in primes:
        if is_left_truncatable_prime(prime) and is_right_truncatable_prime(prime):
            ltr_primes.append(prime)
    return sorted(ltr_primes)