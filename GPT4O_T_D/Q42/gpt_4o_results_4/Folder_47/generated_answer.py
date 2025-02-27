def prime_factors(lst):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        return factors
    if len(lst) > 34:
        return get_prime_factors(lst[34])
    return set()