def prime_factors(numbers):
    number = numbers[2]
    factors = set()
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.add(divisor)
            number = number / divisor
        else:
            divisor += 1
    return factors