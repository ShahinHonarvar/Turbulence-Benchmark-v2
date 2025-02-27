def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0 and is_prime(i):
                factors.add(i)
        if num % 2 == 0:
            factors.add(2)
        if num % 3 == 0:
            factors.add(3)
        return factors
    return get_prime_factors(numbers[312])