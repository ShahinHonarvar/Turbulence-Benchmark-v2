import math

def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(math.sqrt(n)) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors
    return get_factors(numbers[849])