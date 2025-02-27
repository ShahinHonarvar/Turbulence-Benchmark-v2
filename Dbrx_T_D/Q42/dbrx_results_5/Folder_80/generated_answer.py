def prime_factors(numbers):
    return {factor for number in [numbers[746]] for factor in {i for i in range(2, number + 1) if number % i == 0 and all((i % j != 0 for j in range(2, i)))}}