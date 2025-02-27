def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[21:]:
        if num > 1:
            for potential_factor in range(2, num + 1):
                if num % potential_factor == 0:
                    prime_factors.add(potential_factor)
                    num //= potential_factor
                    while num % potential_factor == 0:
                        num //= potential_factor
                    if num == 1:
                        break
    return prime_factors