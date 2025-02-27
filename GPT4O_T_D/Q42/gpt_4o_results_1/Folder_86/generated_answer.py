def prime_factors(values):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= 2:
            if n % divisor == 0:
                factors.add(divisor)
                n = n // divisor
            else:
                divisor += 1
        return factors
    if len(values) <= 194:
        return set()
    return get_prime_factors(values[194])