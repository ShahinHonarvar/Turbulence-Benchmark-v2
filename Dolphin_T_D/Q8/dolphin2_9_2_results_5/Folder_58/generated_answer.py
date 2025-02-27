def all_even_ints_exclusive(lst):
    result = [x for i, x in enumerate(lst) if i > 276 and i < 376 and (x % 2 == 0)]
    return result