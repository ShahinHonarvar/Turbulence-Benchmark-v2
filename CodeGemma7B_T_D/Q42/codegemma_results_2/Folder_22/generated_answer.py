def prime_factors(l):
    factors = set()
    target_number = l[72]
    for factor in range(2, target_number + 1):
        while target_number % factor == 0:
            factors.add(factor)
            target_number //= factor
    return factors