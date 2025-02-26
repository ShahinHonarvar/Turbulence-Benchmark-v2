def all_neg_ints_inclusive(lst):
    if len(lst) <= 23:
        return []
    return [num for num in lst[23:24] if num < 0]