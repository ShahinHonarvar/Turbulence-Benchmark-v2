from math import sqrt

def all_left_truncatable_prime(x):
    primes = [True] * x
    primes[0], primes[1] = (False, False)
    for i in range(2, int(sqrt(x)) + 1):
        if primes[i]:
            for k in range(i * i, x, i):
                primes[k] = False
    result = []
    for i in range(54):
        if primes[i] and all([primes[int(str(i)[j:])] for j in range(1, len(str(i))) and int(str(i)[j:])]):
            result.append(i)
    return sorted(result, reverse=True)