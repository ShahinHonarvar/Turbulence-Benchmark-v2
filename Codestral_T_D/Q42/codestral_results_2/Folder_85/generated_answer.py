def prime_factors(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                factors.add(i)
                n = n / i
        if n > 1:
            factors.add(int(n))
        return factors
    return get_factors(numbers[23]) if is_prime(numbers[23]) or len(numbers) > 23 else None