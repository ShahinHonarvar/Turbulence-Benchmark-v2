def all_left_right_truncatable_prime(t):
    x = t[49]
    primes = []
    for possiblePrime in range(2, x + 1):
        if all((prime_check(possiblePrime, i) for i in range(1, len(str(possiblePrime))))):
            primes.append(possiblePrime)
    return sorted(primes)

def prime_check(n, i):
    return is_prime(int(str(n)[i:])) and is_prime(int(str(n)[:-i]))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True