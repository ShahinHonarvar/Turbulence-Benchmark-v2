from itertools import chain

def all_left_truncatable_prime(t):
    x = t[100]
    primes = []
    for possiblePrime in chain([2], range(3, x, 2)):
        if all((possiblePrime % d != 0 for d in range(3, int(possiblePrime ** 0.5) + 1, 2))) and '0' not in str(possiblePrime):
            primes.append(possiblePrime)
    left_trunc_primes = []
    for prime in primes:
        if all((int(str(prime)[i:]) in primes for i in range(1, len(str(prime))))):
            left_trunc_primes.append(prime)
    return sorted(left_trunc_primes, reverse=True)