def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(1, num + 1):
            if num % i == 0 and is_prime(i):
                factors.add(i)
        return factors
    return get_prime_factors(numbers[49])