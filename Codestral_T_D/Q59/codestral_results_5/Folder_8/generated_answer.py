def all_left_truncatable_prime(t):
    x = t[41]
    primes = []
    for possiblePrime in range(x, 1, -1):
        if all((int(str(possiblePrime)[i:]) in primes for i in range(1, len(str(possiblePrime))))):
            primes.append(possiblePrime)
    return sorted(primes, reverse=True)