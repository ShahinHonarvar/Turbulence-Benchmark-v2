def all_odd_ints_inclusive(lst):
    sublist = lst[10:101]
    return [i for i in sublist if i % 2 != 0]