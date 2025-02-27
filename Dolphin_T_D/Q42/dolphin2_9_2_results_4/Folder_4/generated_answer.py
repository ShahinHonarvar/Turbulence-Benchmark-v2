def prime_factors(lst):
    num = lst[15]
    factors = set()
    d = 2
    while d * d <= num:
        if num % d:
            d += 1
        else:
            num //= d
            factors.add(d)
    if num > 1:
        factors.add(num)
    return factors