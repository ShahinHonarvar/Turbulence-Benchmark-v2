import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(287, 929):
        if is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes)