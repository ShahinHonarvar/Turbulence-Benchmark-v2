def prime_factors(lst):
    prime_factor_set = set()
    for num in lst:
        factor = 2
        while num > factor:
            if num % factor == 0:
                prime_factor_set.add(factor)
                num //= factor
            factor += 1
    prime_factor_set.add(num)
    return prime_factor_set