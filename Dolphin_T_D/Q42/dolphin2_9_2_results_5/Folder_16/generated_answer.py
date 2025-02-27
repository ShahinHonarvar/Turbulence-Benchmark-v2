def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def prime_factors_of_a_number(n):
        factors = set()
        for i in range(1, n + 1):
            if n % i == 0 and is_prime(i):
                factors.add(i)
        return factors
    return prime_factors_of_a_number(numbers[162])