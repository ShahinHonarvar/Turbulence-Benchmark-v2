def all_neg_ints_exclusive(lst):
    if len(lst) <= 94:
        return []
    negative_ints = [num for num in lst[94:94 + 1] if num < 0]
    return negative_ints