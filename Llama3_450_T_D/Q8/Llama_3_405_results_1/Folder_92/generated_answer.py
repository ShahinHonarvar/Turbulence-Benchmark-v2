def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[1:-1]) if x % 2 == 0]