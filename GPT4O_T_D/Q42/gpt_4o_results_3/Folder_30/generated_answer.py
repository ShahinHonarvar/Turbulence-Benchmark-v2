def prime_factors(numbers):

    def get_prime_factors(n):
        factor = 2
        factors = set()
        while factor * factor <= n:
            while n % factor == 0:
                factors.add(factor)
                n //= factor
            factor += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(numbers) <= 94:
        return set()
    return get_prime_factors(numbers[94])