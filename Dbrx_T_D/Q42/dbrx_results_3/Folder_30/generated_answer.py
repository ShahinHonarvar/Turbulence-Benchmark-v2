def prime_factors(numbers):
    return set(prime_factors_for_number(numbers[94]))

def prime_factors_for_number(number):
    factors = []
    i = 2
    while i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    return factors