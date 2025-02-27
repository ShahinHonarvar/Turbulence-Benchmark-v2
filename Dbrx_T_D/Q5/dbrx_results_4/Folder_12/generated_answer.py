def all_neg_ints_inclusive(lst):
    if len(lst) < 64:
        return []
    return [num for num in lst[14:65] if num < 0]