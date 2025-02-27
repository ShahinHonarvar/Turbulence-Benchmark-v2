import math

def prime_factors(lst):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of_num(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i:
                continue
            if is_prime(i):
                factors.add(i)
            if i != n // i:
                if is_prime(n // i):
                    factors.add(n // i)
        return factors
    return prime_factors_of_num(lst[851])