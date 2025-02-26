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
        return factors
    if len(numbers) < 3:
        return set()
    num = numbers[2]
    factors = get_factors(num)
    return {factor for factor in factors if is_prime(factor)}