def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        if is_prime(n):
            return {n}
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return factors(i) | factors(n // i)
        return set()
    return factors(lst[94])