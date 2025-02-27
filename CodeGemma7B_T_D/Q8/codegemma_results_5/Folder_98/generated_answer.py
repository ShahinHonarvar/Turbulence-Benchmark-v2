def all_even_ints_exclusive(lst):
    return [i for i in lst if isinstance(i, int) and i % 2 == 0 and (i not in range(0, 7))]