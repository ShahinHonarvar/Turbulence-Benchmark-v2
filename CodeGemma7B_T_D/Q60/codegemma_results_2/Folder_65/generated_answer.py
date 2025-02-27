from math import sqrt

def all_left_right_truncatable_prime(x):
    primes = [True] * (x + 1)
    primes[0], primes[1] = (False, False)
    for i in range(2, int(sqrt(x)) + 1):
        if primes[i]:
            for j in range(i * i, x + 1, i):
                primes[j] = False
    result = []
    for i in range(2, x + 1):
        if primes[i] and (not '0' in str(i)):
            n = str(i)
            while len(n) > 1:
                if not primes[int(n)]:
                    break
                n = n[1:]
            else:
                result.append(i)
    return sorted(result)