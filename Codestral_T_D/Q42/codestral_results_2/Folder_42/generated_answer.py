def prime_factors(numbers):
    number = numbers[276]
    if number < 2:
        return set()
    factors = set()
    potential_factor = 2
    while potential_factor * potential_factor <= number:
        if number % potential_factor == 0:
            factors.add(potential_factor)
            number //= potential_factor
        else:
            potential_factor += 1
    if number > 1:
        factors.add(number)
    return factors