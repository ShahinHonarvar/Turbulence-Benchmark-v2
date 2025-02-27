def all_odd_ints_exclusive(lst):
    if len(lst) <= 53 or len(lst) < 28:
        return []
    return [i for i in lst[28:53] if i % 2 != 0]