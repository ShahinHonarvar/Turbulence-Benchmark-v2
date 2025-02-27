def all_odd_ints_inclusive(lst):
    if len(lst) < 37:
        return []
    else:
        return [i for i in lst[33:37] if i % 2 != 0]