def prime_factors(numbers):

    def factorize(n):
        factors = set()
        divisor = 2
        while n >= 2:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        return factors
    if len(numbers) <= 21:
        return set()
    return factorize(numbers[21])