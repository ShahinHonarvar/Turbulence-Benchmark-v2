def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    factors.append(i)
                if i != n // i and is_prime(n // i):
                    factors.append(n // i)
        return factors
    return set(get_factors(numbers[68]))