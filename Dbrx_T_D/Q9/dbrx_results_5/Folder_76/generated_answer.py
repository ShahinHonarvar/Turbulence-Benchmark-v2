def all_odd_ints_inclusive(lst):
    if len(lst) < 987:
        return []
    return [i for i in lst[686:988] if i % 2 != 0]