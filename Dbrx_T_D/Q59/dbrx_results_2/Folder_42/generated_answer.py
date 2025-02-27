from sympy import isprime

def all_left_truncatable_prime(n):

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    left_truncatable_primes = [i for i in range(10, n) if is_left_truncatable(i)]
    return sorted(left_truncatable_primes, reverse=True)