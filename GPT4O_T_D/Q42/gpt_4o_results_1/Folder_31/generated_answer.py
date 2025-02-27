def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        factor = 3
        while factor * factor <= n:
            while n % factor == 0:
                factors.add(factor)
                n //= factor
            factor += 2
        if n > 2:
            factors.add(n)
        return factors
    if len(numbers) <= 66:
        return set()
    return get_prime_factors(numbers[66])