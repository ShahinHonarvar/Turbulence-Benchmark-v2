def prime_factors(numbers):
    return {i for i in set(numbers) if all((i % j != 0 for j in range(2, i)))}