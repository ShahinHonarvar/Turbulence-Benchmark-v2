def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return {i for i in range(2, numbers[16] + 1) if numbers[16] % i == 0 and is_prime(i)}