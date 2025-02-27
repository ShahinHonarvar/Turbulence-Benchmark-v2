def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        d = 2
        while n >= d:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1
        return factors
    if len(numbers) > 993:
        return get_prime_factors(numbers[993])
    return set()