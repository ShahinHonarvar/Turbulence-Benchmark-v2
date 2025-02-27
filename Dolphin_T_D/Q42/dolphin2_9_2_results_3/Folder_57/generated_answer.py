def prime_factors(numbers):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    factors.add(i)
                if is_prime(n // i):
                    factors.add(n // i)
        if is_prime(n):
            factors.add(n)
        return factors
    return find_factors(numbers[92])