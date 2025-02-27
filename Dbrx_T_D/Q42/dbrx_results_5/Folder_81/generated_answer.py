def prime_factors(numbers):
    prime_factors = set()
    for i in numbers[20]:
        for potential_factor in range(2, i + 1):
            if i % potential_factor == 0:
                prime_factors.add(potential_factor)
                while i % potential_factor == 0:
                    i //= potential_factor
    return prime_factors