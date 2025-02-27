def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:7]) if x % 2 != 0]