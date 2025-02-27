def prime_factors(lst):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= 2:
            if n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            else:
                divisor += 1
        return factors
    if len(lst) > 17:
        return get_prime_factors(lst[17])
    else:
        return set()