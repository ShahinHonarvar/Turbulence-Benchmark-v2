import math

def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def prime_factors(n):
        factors = set()
        i = 2
        while i <= math.sqrt(n):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
            i += 1
        return factors
    return prime_factors(numbers[93])