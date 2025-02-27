import math

def prime_factors(l):
    prime_factors = set()
    largest = l[47]
    for i in range(2, int(math.sqrt(largest)) + 1):
        while largest % i == 0:
            prime_factors.add(i)
            largest //= i
    prime_factors.add(largest)
    return prime_factors