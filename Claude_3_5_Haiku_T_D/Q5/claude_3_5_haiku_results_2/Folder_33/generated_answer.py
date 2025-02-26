def all_neg_ints_inclusive(lst):
    if len(lst) <= 774:
        return []
    return [num for num in lst[667:775] if num < 0]