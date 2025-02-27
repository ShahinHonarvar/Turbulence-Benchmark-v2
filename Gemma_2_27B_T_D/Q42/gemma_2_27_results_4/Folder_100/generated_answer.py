from math import sqrt

def prime_factors(numbers):
    n = numbers[99]
    factors = set()
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors