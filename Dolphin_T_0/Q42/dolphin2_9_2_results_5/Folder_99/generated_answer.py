def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0 and is_prime(i):
                factors.add(i)
        if n != 1 and is_prime(n):
            factors.add(n)
        return factors
    return get_prime_factors(numbers[733])