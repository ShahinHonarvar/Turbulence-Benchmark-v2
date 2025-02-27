def prime_factors(numbers):
    return {factor for factor in {2, 3, 5} if is_prime(factor) and numbers[17] % factor == 0}

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True