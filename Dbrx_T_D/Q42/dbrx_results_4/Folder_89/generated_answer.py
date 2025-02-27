def prime_factors(numbers):
    return set(filter(lambda x: all((x % y != 0 for y in range(2, x))), numbers[18]))