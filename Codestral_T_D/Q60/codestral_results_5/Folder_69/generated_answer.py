def all_left_right_truncatable_prime(t):
    x = t[760]
    primes = []
    for possiblePrime in range(2, x + 1):
        if all((int(possiblePrime[i:]) in primes or (is_prime(int(possiblePrime[i:])) and int(possiblePrime[:i]) in primes) or is_prime(int(possiblePrime[:i])) for i in range(1, len(str(possiblePrime))))):
            primes.append(possiblePrime)
    primes.sort(reverse=True)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True