def prime_factors(lst):
    lst[48] = max(lst)
    return set([y for i in lst for y in range(2, i + 1) if i % y == 0])