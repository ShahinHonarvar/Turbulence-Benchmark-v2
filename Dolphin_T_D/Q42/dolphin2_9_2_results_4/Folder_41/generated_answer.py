def prime_factors(numbers):

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return set((factor for number in numbers for factor in (i for i in range(1, numbers[84] + 1) if numbers[84] % i == 0 and is_prime(i))))