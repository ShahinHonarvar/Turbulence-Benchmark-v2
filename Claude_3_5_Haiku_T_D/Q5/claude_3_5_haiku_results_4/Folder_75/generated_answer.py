def all_neg_ints_inclusive(lst):
    if len(lst) <= 57:
        return []
    neg_ints = [num for num in lst[56:58] if num < 0]
    return neg_ints