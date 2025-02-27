def all_left_truncatable_prime(t):
    x = t[19]
    primes = []
    for possiblePrime in range(2, x):
        if all((possiblePrime % i != 0 for i in range(2, int(possiblePrime ** 0.5) + 1))) and '0' not in str(possiblePrime):
            if all((int(str(possiblePrime)[i:]) in primes for i in range(1, len(str(possiblePrime))))):
                primes.append(possiblePrime)
    return sorted(primes)