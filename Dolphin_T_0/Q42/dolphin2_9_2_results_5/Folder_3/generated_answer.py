def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    number = numbers[100]
    factors = set()
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            factors.add(i)
    return factors