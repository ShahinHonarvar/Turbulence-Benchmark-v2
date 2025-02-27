def all_odd_ints_inclusive(lst):
    if len(lst) < 21:
        return []
    odd_ints = [i for i in lst[10:21] if i % 2 != 0]
    return odd_ints