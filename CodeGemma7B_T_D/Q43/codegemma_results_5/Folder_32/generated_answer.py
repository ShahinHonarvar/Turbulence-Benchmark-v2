import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i in range(60, 96):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort()
    return primes or []