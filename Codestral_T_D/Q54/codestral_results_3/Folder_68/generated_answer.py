def all_right_truncatable_prime(t):
    x = t[1]
    primes = []
    for possiblePrime in range(2, x):
        if all((possiblePrime % i != 0 for i in range(2, int(possiblePrime ** 0.5) + 1))):
            num = possiblePrime
            while num > 0:
                if num not in primes:
                    break
                num //= 10
            else:
                primes.append(possiblePrime)
    return sorted(primes, reverse=True)