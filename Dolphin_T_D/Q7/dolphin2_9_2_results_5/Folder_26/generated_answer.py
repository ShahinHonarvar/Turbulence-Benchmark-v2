def all_even_ints_inclusive(lst):
    evens = [x for i, x in enumerate(lst) if i >= 62 and i <= 99 and (x % 2 == 0)]
    return evens