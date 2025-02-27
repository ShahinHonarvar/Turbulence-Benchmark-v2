import math

def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    index = 64
    number = numbers[index]
    factors = set()
    for i in range(2, number + 1):
        if is_prime(i) and number % i == 0:
            factors.add(i)
    return factors