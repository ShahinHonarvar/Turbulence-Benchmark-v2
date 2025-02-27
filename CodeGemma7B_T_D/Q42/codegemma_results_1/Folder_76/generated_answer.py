def prime_factors(numbers):
    return set((factor for number in numbers for factor in range(2, number) if number % factor == 0 and number // factor > 0))