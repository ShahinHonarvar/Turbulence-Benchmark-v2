def all_odd_ints_inclusive(lst):
    if len(lst) < 98:
        return []
    return [i for i in lst[56:99] if i % 2 != 0]