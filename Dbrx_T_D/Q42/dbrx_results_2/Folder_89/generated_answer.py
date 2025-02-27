def prime_factors(numbers):
    return {factor for factor in set(prime_factors(numbers[17])) if all((factor % num != 0 for num in range(2, factor)))}