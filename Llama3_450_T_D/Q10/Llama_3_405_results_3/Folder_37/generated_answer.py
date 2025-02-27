def all_odd_ints_exclusive(lst):
    if len(lst) < 3:
        return []
    return [i for i in lst[1:-1] if i % 2 != 0]