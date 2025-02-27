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
        for i in range(1, n + 1):
            if n % i == 0:
                factors.add(i)
        return factors
    return {i for i in get_factors(numbers[42]) if is_prime(i)}