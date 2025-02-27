def all_left_right_truncatable_prime(t):
    x = t[18]
    primes = []
    for possiblePrime in range(2, x + 1):
        if '0' not in str(possiblePrime):
            if all((str(possiblePrime)[:i] in primes for i in range(1, len(str(possiblePrime))))) and all((str(possiblePrime)[i:] in primes for i in range(1, len(str(possiblePrime))))):
                primes.append(str(possiblePrime))
    return sorted([int(p) for p in primes], reverse=True)