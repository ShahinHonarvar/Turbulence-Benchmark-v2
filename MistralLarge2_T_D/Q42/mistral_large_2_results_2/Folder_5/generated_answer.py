def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                if is_prime(d):
                    factors.add(d)
                n //= d
            d += 1
        if n > 1 and is_prime(n):
            factors.add(n)
        return factors
    if len(numbers) > 67:
        return get_prime_factors(numbers[67])
    else:
        return set()