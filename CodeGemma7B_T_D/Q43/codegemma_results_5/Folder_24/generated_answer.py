from math import sqrt

def find_primes_between_indices(numbers):
    primes = []
    for i in range(38, 56):
        if all((i % j != 0 for j in range(2, int(sqrt(i)) + 1))):
            primes.append(i)
    primes.sort(reverse=True)
    return primes or []