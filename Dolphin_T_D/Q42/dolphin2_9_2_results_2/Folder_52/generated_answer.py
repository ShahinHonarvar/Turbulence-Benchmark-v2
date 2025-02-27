def prime_factors(lst):
    number = lst[478]
    factors = set()
    d = 2
    while d * d <= number:
        if number % d == 0:
            factors.add(d)
            number //= d
        else:
            d += 1
    if number > 1:
        factors.add(number)
    return factors