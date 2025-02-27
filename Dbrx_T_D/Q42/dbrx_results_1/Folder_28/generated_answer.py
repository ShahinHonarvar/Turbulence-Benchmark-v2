def prime_factors(numbers):
    return {factor for factor in range(2, numbers[36] // 2 + 2) if numbers[36] % factor == 0 and all((factor % prime != 0 for prime in range(2, int(factor ** 0.5) + 1)))}