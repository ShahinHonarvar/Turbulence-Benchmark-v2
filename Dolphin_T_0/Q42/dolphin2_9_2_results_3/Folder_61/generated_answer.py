def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def prime_factors_of_number(n):
        return {i for i in range(2, n + 1) if n % i == 0 and is_prime(i)}
    return prime_factors_of_number(numbers[8])