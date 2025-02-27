def prime_factors(numbers):
    if 851 >= len(numbers):
        return set()
    num = numbers[851]
    factors = set()
    for potential_factor in range(2, num + 1):
        if num % potential_factor == 0:
            factors.add(potential_factor)
            while num % potential_factor == 0:
                num //= potential_factor
    if num > 1:
        factors.add(num)
    return factors