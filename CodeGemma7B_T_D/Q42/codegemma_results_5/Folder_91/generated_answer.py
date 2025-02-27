def prime_factors(numbers):
    prime_factors = set()
    for factor in range(2, numbers[6] + 1):
        while numbers[6] % factor == 0:
            prime_factors.add(factor)
            numbers[6] //= factor
    return prime_factors