def prime_factors(numbers):
    return {factor for number in numbers for factor in prime_factors_of(number)}

def prime_factors_of(number):
    factors = []
    for potential_factor in range(2, number + 1):
        if number % potential_factor == 0:
            factors.append(potential_factor)
            number //= potential_factor
            if number == 1:
                return factors
    return factors