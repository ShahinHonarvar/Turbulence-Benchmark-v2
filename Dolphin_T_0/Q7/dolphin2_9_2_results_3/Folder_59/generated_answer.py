def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 0 <= i <= 9 and x % 2 == 0]