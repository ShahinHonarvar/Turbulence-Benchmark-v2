def prime_factors(int_list):
    num = int_list[194]
    factors = set()
    d = 2
    while d * d <= num:
        if num % d == 0:
            factors.add(d)
            num = num / d
        else:
            d += 1
    if num > 1:
        factors.add(num)
    return factors