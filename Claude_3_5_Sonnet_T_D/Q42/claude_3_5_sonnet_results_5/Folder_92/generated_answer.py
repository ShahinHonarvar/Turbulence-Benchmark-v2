def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        factors.add(n)
        return factors
    if not numbers:
        return set()
    n = numbers[0]
    all_factors = get_factors(n)
    return {factor for factor in all_factors if is_prime(factor)}