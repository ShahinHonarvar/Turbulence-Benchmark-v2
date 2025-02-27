def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[10:76], 10) if x % 2 == 0]