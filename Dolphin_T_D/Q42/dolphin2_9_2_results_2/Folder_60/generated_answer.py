def prime_factors(num_list):
    num = num_list[88]
    factors = set()
    d = 2
    while d * d <= num:
        while num % d == 0:
            factors.add(d)
            num /= d
        d += 1
    if num > 1:
        factors.add(num)
    return factors