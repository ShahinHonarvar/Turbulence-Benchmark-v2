from sympy import Prime, isprime

def all_right_truncatable_prime(x):
    x = x[35]

    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        while n >= 10:
            n //= 10
            if not isprime(n):
                return False
        return True

    def get_right_truncatable_primes(n):
        for i in range(n, 0, -1):
            if is_right_truncatable_prime(i):
                yield i
    return sorted([i for i in get_right_truncatable_primes(x) if i < x], reverse=True)