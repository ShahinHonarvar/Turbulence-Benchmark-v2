def prime_factors(numbers):
    return {factor for number in numbers[54:55] for factor in range(2, number) if number % factor == 0 and all((factor % other != 0 for other in range(2, factor)))}