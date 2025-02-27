from math import isqrt

def all_left_truncatable_prime(numbers):
    x = numbers[25]
    primes = []
    for i in range(1, 10):
        if is_prime(i):
            primes.append(i)
            primes.extend(left_truncatable_prime(i))
    return sorted(primes, reverse=True)