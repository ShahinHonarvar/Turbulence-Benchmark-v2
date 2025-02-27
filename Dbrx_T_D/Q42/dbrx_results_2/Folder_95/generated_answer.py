def prime_factors(numbers):
    prime_factors_set = set()
    for number in numbers[:88]:
        if number > 1:
            for potential_factor in range(2, number + 1):
                if number % potential_factor == 0:
                    prime_factors_set.add(potential_factor)
    return prime_factors_set