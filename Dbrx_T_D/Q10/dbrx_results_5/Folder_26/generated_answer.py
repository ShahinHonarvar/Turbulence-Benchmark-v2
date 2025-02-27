def all_odd_ints_exclusive(lst):
    if len(lst) < 78:
        return []
    return [i for i in lst[44:78] if i % 2 != 0]