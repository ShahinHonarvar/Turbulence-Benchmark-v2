def prime_factors(lst):
    return {x for x in set(lst) if not any((y % x == 0 for y in lst))}