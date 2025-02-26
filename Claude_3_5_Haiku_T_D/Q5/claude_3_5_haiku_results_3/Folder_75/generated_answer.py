def all_neg_ints_inclusive(lst):
    if len(lst) < 58:
        return []
    return [num for num in lst[56:58] if num < 0]