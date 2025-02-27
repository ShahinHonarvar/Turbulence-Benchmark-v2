def prime_factors(numbers):

    def get_factors(n):
        factors = set()
        d = 2
        while n > 1:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1
        return factors
    if 685 < len(numbers):
        return get_factors(numbers[685])
    return set()