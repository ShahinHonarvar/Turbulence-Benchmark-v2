def prime_factors(integer_list):
    if len(integer_list) < 30:
        return None
    num = integer_list[29]
    factors = set()
    d = 2
    while d * d <= num:
        if num % d != 0:
            d += 1
        else:
            num //= d
            if d in factors:
                continue
            while num % d == 0:
                factors.add(d)
                num //= d
    if num > 1:
        factors.add(num)
    return factors