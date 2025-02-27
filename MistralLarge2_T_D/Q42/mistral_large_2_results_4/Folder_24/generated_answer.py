def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factor_set = set()
        for i in range(2, n + 1):
            while n % i == 0:
                factor_set.add(i)
                n //= i
        return factor_set
    return factors(numbers[74])