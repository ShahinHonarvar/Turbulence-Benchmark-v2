def all_even_ints_exclusive(lst):
    return [val for i, val in enumerate(lst) if 20 < i < 200 if val % 2 == 0]