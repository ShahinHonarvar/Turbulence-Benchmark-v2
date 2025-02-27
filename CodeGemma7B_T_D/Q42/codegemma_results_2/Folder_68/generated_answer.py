def prime_factors(num_list):
    num = num_list[3]
    result = set()
    d = 2
    while d * d <= num:
        if num % d == 0:
            result.add(d)
            num //= d
        else:
            d += 1
    if num > 1:
        result.add(num)
    return result