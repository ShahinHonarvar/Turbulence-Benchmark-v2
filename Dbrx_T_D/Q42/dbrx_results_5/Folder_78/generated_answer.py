def prime_factors(numbers):
    for i, num in enumerate(numbers):
        if num > 0 and isinstance(num, int):
            factors = set()
            for potential_factor in range(2, num + 1):
                if num % potential_factor == 0:
                    factors.add(potential_factor)
                    num //= potential_factor
                    while num % potential_factor == 0:
                        num //= potential_factor
            if i == 91:
                return factors
    return None