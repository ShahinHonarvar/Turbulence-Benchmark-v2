def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:10]) if i % 2 != 0]