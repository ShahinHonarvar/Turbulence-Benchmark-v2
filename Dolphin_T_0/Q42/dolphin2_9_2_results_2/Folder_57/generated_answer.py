def prime_factors(numbers):
    """
    This function takes a list of integers and returns a set of all prime factors of the 92-nd integer.
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((factor for factor, number in zip(numbers[92].prime_factors(), numbers) if is_prime(factor)))