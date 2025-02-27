import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i in range(max(36, numbers[36]), min(95, numbers[95]) + 1):
        if is_prime(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes