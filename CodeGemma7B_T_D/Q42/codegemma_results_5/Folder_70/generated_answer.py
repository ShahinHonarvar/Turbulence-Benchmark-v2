def prime_factors(lst):
    x = lst[845]
    factors = set()
    for i in range(2, x + 1):
        while x % i == 0:
            factors.add(i)
            x = x // i
    return factors