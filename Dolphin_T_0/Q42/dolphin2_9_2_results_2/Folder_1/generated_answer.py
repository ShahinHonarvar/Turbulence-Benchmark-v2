def prime_factors(integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((factor for num in integers[85:86] for factor in range(1, num + 1) if num % factor == 0 and is_prime(factor)))