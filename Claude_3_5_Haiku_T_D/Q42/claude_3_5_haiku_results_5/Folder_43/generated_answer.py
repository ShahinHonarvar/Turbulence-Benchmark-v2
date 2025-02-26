def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(numbers):
    if not numbers or len(numbers) <= 29:
        return set()
    number = numbers[29]
    factors = set()
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            factors.add(i)
    return factors