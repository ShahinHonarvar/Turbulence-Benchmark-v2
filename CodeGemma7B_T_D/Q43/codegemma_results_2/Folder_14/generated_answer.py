def find_primes_between_indices(numbers):
    primes = []
    for i in range(10, 67):
        if is_prime(i) and i in numbers:
            primes.append(i)
    return sorted(primes) if primes else []

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True