def prime_factors(lst):
    n = lst[51]
    factors = set()
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.add(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors