def prime_factors(lst):

    def factorize(n):
        factors = set()
        divisor = 2
        while n >= 2:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        return factors
    if len(lst) < 69:
        return set()
    return factorize(lst[68])