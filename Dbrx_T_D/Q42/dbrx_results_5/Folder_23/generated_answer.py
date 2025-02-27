def prime_factors(numbers):
    if len(numbers) <= 69:
        return 'Input list should have at least 70 elements.'
    target_number = numbers[69]
    i = 2
    factors = set()
    while i * i <= target_number:
        if target_number % i:
            i += 1
        else:
            target_number //= i
            factors.add(i)
    if target_number > 1:
        factors.add(target_number)
    return factors