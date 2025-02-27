def prime_factors(numbers):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return {i for i in range(2, numbers[19] + 1) if numbers[19] % i == 0 and is_prime(i)}