def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    target_number = numbers[926]
    factors = set()
    for factor in range(1, target_number + 1):
        if target_number % factor == 0 and is_prime(factor):
            factors.add(factor)
    return factors