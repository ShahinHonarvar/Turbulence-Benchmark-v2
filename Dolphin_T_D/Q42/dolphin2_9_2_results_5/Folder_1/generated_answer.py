def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((factor for number in numbers for factor in range(2, number + 1) if is_prime(factor) and number % factor == 0))