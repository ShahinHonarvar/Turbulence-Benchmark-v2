def prime_factors(numbers):
    i = numbers[19]
    factors = set()
    for potential_factor in range(2, i + 1):
        if i % potential_factor == 0:
            factors.add(potential_factor)
            i //= potential_factor
    return factors