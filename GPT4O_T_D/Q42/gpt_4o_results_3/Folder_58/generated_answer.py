def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        return factors
    if 714 < len(numbers):
        return get_prime_factors(numbers[714])
    return set()