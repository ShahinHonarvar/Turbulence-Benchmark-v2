def all_odd_ints_inclusive(lst):
    if len(lst) < 93:
        return []
    odd_ints = [i for i in lst[66:94] if i % 2 != 0]
    return odd_ints