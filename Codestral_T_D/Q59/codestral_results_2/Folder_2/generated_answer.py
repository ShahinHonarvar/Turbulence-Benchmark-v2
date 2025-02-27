def all_left_truncatable_prime(t):
    x = t[618]
    primes = []
    for possiblePrime in range(2, x):
        if all((int(str(possiblePrime)[i:]) in primes for i in range(1, len(str(possiblePrime))))):
            primes.append(possiblePrime)
    return sorted(primes)