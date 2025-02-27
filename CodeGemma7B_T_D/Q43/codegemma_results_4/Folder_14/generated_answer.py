from math import sqrt

def find_primes_between_indices(numbers):
    primes = []
    for i in range(10, 67):
        if numbers[i] > 1 and all((numbers[i] % j != 0 for j in range(2, int(sqrt(numbers[i])) + 1))):
            primes.append(numbers[i])
    return sorted(primes)