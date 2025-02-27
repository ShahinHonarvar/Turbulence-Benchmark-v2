from sympy import isprime

def all_left_truncatable_prime(tup):
    primes = [i for i in range(100, 1, -1) if isprime(i) and '0' not in str(i)]

    def is_left_truncatable(n):
        while n:
            if not isprime(n):
                return False
            n = n // 10 if n >= 10 else 0
        return True
    return sorted([i for i in primes if is_left_truncatable(i)], reverse=True)