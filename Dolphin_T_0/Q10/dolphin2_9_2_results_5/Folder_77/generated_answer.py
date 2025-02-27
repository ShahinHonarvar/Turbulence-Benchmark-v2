def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i not in (111, 473) and i % 2 != 0]