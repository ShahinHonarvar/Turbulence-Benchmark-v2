def prime_factors(numbers):
    prime_factors = set()
    for i in range(len(numbers)):
        num = numbers[i]
        if num > 1:
            for potential_factor in range(2, num + 1):
                if num % potential_factor == 0:
                    prime_factors.add(potential_factor)
                    num = num // potential_factor
                    while num % potential_factor == 0:
                        num = num // potential_factor
    return prime_factors