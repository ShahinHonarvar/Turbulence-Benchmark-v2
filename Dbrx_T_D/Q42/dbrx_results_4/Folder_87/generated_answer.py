def prime_factors(numbers):
    return {factor for number in numbers for factor in set(prime_factors(number)) if number % factor == 0 and is_prime(factor)}

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True