def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(numbers) > 17:
        return get_prime_factors(numbers[17])
    return set()