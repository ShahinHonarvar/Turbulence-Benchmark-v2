def prime_factors(numbers):
    prime_factors = set()
    number = numbers[162]
    for divisor in range(2, number + 1):
        while number % divisor == 0:
            prime_factors.add(divisor)
            number //= divisor
    return prime_factors