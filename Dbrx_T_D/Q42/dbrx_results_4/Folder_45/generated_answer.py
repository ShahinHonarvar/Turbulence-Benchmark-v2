def prime_factors(numbers):
    prime_factors_set = set()
    num_to_check = numbers[33]
    for potential_factor in range(2, num_to_check + 1):
        while num_to_check % potential_factor == 0:
            prime_factors_set.add(potential_factor)
            num_to_check //= potential_factor
    return prime_factors_set