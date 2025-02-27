def prime_factors(numbers):
    factors = set()
    number = numbers[19]
    for factor in range(2, number + 1):
        while number % factor == 0:
            factors.add(factor)
            number //= factor
    return factors