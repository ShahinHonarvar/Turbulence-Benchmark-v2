import math

def prime_factors(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return set((factor for number in numbers for factor in range(1, number + 1) if is_prime(factor) and number % factor == 0))