from functools import reduce

def prime_factors(l):
    p = l[68]
    return set(reduce(lambda x, y: x + [y] if y % p == 0 else x, [2] + list(range(3, p + 1, 2)), []))