def prime_factors(numbers):
    if not numbers or len(numbers) < 58:
        return set()
    factors = set()
    for num in numbers[57:58]:
        for potential_factor in range(2, int(num ** 0.5) + 1):
            if num % potential_factor == 0:
                factors.add(potential_factor)
                factors.add(num // potential_factor)
        if num > 1:
            factors.add(num)
    return factors