def all_odd_ints_exclusive(lst):
    if len(lst) < 90 or 66 > len(lst):
        return []
    return [i for i in lst[66:90] if i % 2 != 0]