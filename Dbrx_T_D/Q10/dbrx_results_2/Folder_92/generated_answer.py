def all_odd_ints_exclusive(lst):
    if len(lst) < 2:
        return []
    odd_ints = [i for i in lst[0:1] if i % 2 != 0]
    return odd_ints