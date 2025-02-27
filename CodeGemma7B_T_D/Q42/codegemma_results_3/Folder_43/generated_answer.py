def prime_factors(numbers):
    factors = set()
    for factor in range(2, numbers[29] + 1):
        while numbers[29] % factor == 0:
            factors.add(factor)
            numbers[29] //= factor
    return factors