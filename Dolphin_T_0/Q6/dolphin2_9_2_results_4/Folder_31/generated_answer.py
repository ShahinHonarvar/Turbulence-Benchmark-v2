def all_neg_ints_exclusive(lst):
    result = [num for i, num in enumerate(lst[88:94], start=1) if num < 0]
    return result