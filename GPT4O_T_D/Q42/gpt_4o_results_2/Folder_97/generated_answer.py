def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        divider = 2
        while n % divider == 0:
            factors.add(divider)
            n //= divider
        divider = 3
        while divider * divider <= n:
            while n % divider == 0:
                factors.add(divider)
                n //= divider
            divider += 2
        if n > 2:
            factors.add(n)
        return factors
    if 132 < len(numbers):
        return get_prime_factors(numbers[132])
    return set()