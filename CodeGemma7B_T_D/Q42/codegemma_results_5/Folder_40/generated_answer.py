def prime_factors(numbers):
    prime_factors = set()
    number = numbers[7]
    for factor in range(2, number + 1):
        while number % factor == 0:
            prime_factors.add(factor)
            number //= factor
    return prime_factors