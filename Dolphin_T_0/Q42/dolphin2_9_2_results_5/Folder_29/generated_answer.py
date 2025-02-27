def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((i for i in range(2, numbers[19] + 1) if is_prime(i) and numbers[19] % i == 0))