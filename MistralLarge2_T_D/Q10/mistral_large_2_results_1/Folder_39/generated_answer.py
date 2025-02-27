def all_odd_ints_exclusive(lst):
    return [i for idx, i in enumerate(lst) if idx > 43 and idx < 99 and (i % 2 != 0)]