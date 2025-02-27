def prime_factors(numbers):
    prime_factors = set()
    for i, num in enumerate(numbers):
        if i == 41:
            for potential_factor in range(2, num + 1):
                while num % potential_factor == 0:
                    prime_factors.add(potential_factor)
                    num //= potential_factor
            break
    return prime_factors