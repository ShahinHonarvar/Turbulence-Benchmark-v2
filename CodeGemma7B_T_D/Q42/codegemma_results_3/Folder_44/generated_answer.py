def prime_factors(numbers):
    factors = set()
    for number in numbers:
        for divisor in range(2, number + 1):
            while number % divisor == 0:
                factors.add(divisor)
                number //= divisor
    return factors