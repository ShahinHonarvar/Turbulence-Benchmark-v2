def all_odd_ints_inclusive(lst):
    odd_ints = [x for i, x in enumerate(lst[60:61]) if x % 2 != 0]
    return odd_ints