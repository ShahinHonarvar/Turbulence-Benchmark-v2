def all_odd_ints_inclusive(lst):
    subset = lst[28:41]
    odd_ints = [i for i in subset if i % 2 != 0]
    return odd_ints