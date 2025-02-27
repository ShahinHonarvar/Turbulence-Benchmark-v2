def prime_factors(lst):
    num = lst[276]
    factors = set()
    d = 2
    while d * d <= num:
        if num % d == 0:
            factors.add(d)
            num //= d
        else:
            d += 1
    if num > 1:
        factors.add(num)
    return factors