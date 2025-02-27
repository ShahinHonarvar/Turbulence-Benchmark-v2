def prime_factors(numbers):
    prime_factors_set = set()
    number = numbers[85]
    for factor in range(2, number + 1):
        while number % factor == 0:
            prime_factors_set.add(factor)
            number //= factor
    return prime_factors_set