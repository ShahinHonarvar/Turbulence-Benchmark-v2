from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[6]
    if x < 11:
        return []

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n % (10 * (n // 10))
        return True
    left_truncatable_primes = {i for i in range(11, x + 1) if is_left_truncatable(i)}
    right_truncatable_primes = {i for i in range(11, x + 1) if is_right_truncatable(i)}
    result = []
    for prime in left_truncatable_primes & right_truncatable_primes:
        result.append(prime)
    return sorted(result, reverse=True)