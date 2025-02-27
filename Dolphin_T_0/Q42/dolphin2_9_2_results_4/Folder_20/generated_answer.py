def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(1, n):
            if n % i == 0:
                factors.add(i)
        return factors
    return get_factors(numbers[53])