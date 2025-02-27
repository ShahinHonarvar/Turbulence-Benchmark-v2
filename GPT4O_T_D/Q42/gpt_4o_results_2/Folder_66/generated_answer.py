def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= divisor:
            if n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            else:
                divisor += 1
        return factors
    if len(numbers) <= 42:
        return set()
    return get_prime_factors(numbers[42])