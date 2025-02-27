import math

def all_right_truncatable_prime(x):
    primes = [True] * x
    for i in range(2, int(math.sqrt(x)) + 1):
        if primes[i]:
            for j in range(i * i, x, i):
                primes[j] = False
    truncatable_primes = []
    for i in range(2, x):
        if primes[i]:
            digits = list(str(i))
            for j in range(1, len(digits)):
                number = int(''.join(digits[:-j]))
                if number in primes and primes[number]:
                    truncatable_primes.append(i)
    return sorted(truncatable_primes)