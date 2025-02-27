def prime_factors(numbers):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    def prime_factors_of(number):
        factors = set()
        for i in range(2, number + 1):
            if is_prime(i) and number % i == 0:
                factors.add(i)
        return factors
    return prime_factors_of(numbers[7])