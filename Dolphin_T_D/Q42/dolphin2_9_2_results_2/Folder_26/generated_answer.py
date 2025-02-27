def prime_factors(numbers):

    def _is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def _prime_factors(num):
        factors = set()
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0 and _is_prime(i):
                factors.add(i)
        return factors
    return _prime_factors(numbers[222])