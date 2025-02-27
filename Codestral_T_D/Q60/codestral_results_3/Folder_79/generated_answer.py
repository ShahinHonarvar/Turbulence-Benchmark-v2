def all_left_right_truncatable_prime(t):
    x = t[91]
    primes = []
    for possiblePrime in range(2, x + 1):
        if all((int(str(possiblePrime)[:i]) in primes for i in range(1, len(str(possiblePrime))))):
            primes.append(possiblePrime)
    return primes