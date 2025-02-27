import math

def find_primes_between_indices(nums):
    primes = []
    for i in range(25, 73):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True