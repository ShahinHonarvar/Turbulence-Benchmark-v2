def all_neg_ints_inclusive(lst):
    if len(lst) < 81:
        return []
    return [num for num in lst[40:81] if num < 0]