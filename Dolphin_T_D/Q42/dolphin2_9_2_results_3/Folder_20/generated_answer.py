def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((factor for factor in range(1, lst[53] + 1) if lst[53] % factor == 0 and is_prime(factor)))