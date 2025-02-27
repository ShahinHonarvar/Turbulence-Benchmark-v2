def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= 2:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        return factors
    if len(numbers) > 990:
        return get_prime_factors(numbers[990])
    return set()