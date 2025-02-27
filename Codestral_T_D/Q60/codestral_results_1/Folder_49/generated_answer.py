def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    primes = []
    for possiblePrime in range(2, x + 1):
        if all((int(possiblePrime[i:]) in primes for i in range(len(possiblePrime)))) and all((int(possiblePrime[:i]) in primes for i in range(1, len(possiblePrime)))):
            primes.append(possiblePrime)
    return sorted(primes)