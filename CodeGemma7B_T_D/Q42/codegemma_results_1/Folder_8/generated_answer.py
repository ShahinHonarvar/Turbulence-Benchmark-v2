def prime_factors(args):
    factor = set()
    for num in args:
        for div in range(2, int(num ** 0.5) + 1):
            if not num % div:
                factor.add(div)
                num //= div
        if num > 1:
            factor.add(num)
    return factor