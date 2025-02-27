def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    factors = set()
    for number in numbers:
        if is_prime(number):
            factors.add(number)
    return factors