def prime_factors(numbers):
    if len(numbers) <= 28:
        return set()
    n = numbers[28]
    factors = set()
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor += 1
    return factors