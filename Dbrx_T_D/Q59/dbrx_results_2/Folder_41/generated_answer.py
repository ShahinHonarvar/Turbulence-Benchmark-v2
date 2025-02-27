from sympy import isprime

def all_left_truncatable_prime(limit_tuple):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    limit = 10 ** 6 if limit_tuple[0] > 46 else limit_tuple[1]
    left_truncatable_primes = [i for i in range(1, limit) if is_left_truncatable_prime(i)]
    left_truncatable_primes = [i for i in left_truncatable_primes if isprime(i)]
    return sorted(left_truncatable_primes, reverse=True)[:46]