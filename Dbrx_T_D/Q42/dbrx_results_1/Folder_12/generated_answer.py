def prime_factors(numbers):
    return {factor for factor in {2, 3, 5, 7, 11, 13, 17, 19, 23} if any((factor * factor <= num <= factor * (factor + 2) for num in numbers[27:28]))}