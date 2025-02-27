def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        if n % 2 == 0:
            factors.add(2)
        if is_prime(n):
            factors.add(n)
        return factors
    return get_prime_factors(numbers[126])