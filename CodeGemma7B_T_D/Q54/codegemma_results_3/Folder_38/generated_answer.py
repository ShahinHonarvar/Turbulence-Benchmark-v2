def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    else:
        return True

def sieve_of_erastothenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if primes[p]:
            for multiple in range(p * p, limit + 1, p):
                primes[multiple] = False
    return [p for p in range(limit + 1) if primes[p]]

def all_right_truncatable_prime(tup):
    x = tup[28]
    primes = sieve_of_erastothenes(x)
    result = []
    for prime in primes:
        if is_prime(prime):
            digits = str(prime)
            for i in range(1, len(digits)):
                if not is_prime(int(digits[:-i])):
                    break
            else:
                result.append(prime)
    return sorted(result)