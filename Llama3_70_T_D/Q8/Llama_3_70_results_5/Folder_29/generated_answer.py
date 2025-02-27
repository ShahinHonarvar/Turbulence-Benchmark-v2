def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[49:76], start=49) if x % 2 == 0]