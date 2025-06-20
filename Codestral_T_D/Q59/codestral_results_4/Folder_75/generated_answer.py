def all_left_truncatable_prime(tup):
    x = tup[41]
    primes = []
    for possiblePrime in range(2, x):
        if all((len(str(possiblePrime[i:])) > 0 and is_prime(int(str(possiblePrime[i:]))) for i in range(len(str(possiblePrime))))):
            primes.append(possiblePrime)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True