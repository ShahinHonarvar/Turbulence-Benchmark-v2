def all_right_truncatable_prime(t):
    x = t[37]

    def isprime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n:
            if not isprime(n):
                return False
            n //= 10
        return True
    primes = [n for n in range(x) if isprime(n)]
    return sorted([n for n in primes if is_right_truncatable(n)], reverse=True)