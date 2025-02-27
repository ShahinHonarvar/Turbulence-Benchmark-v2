from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(limit):
    result = []
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in count():
        if i >= limit:
            break
        if primes[i] >= limit:
            break
        if is_prime(int(str(primes[i])[1:])):
            result.append(primes[i])
    return result

def all_left_truncatable_prime(x):
    return sorted(left_truncatable_primes(x))