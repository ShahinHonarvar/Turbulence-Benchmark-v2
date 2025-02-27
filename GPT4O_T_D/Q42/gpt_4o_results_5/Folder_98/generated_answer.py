def prime_factors(numbers):
    if len(numbers) < 5:
        return set()
    num = numbers[4]
    factors = set()
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        divisor += 1
    return factors