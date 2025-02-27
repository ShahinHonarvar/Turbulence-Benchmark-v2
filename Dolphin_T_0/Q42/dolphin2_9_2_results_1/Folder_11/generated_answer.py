import math

def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of_number(n):
        factors = set()
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0 and is_prime(i):
                factors.add(i)
        if n != 1 and is_prime(n):
            factors.add(n)
        return factors
    return prime_factors_of_number(lst[77])