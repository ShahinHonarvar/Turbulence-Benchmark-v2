from functools import reduce

def prime_factors(lst):
    """
    Returns a set of all prime factors of the integer at index 64 of the given list.
    """
    return reduce(lambda x, y: x + y, [factor for factor in range(2, lst[64] + 1) if lst[64] % factor == 0])