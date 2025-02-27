def all_odd_ints_inclusive(lst):
    odd_ints = list(filter(lambda x: x % 2 != 0, lst[10:101]))
    return odd_ints