def prime_factors(numbers):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((factor for factor in range(2, numbers[95]) if is_prime(factor) and numbers[95] % factor == 0))