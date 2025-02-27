def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(numbers) <= 126:
        return set()
    return get_prime_factors(numbers[126])