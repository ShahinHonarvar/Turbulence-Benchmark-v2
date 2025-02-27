def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((fact for num in numbers for fact in range(1, num + 1) if num % fact == 0 and is_prime(fact)))