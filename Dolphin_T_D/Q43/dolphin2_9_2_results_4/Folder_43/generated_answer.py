import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = [numbers[i] for i in range(len(numbers)) if is_prime(numbers[i]) and 31 <= i <= 92]
    return sorted(primes, reverse=True) if primes else []