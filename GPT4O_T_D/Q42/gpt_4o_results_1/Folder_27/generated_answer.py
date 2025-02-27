def prime_factors(lst):

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
    if 0 <= 56 < len(lst):
        return get_prime_factors(lst[56])
    return set()