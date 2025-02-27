def all_neg_ints_exclusive(lst):
    if len(lst) <= 15:
        return []
    return [num for num in lst[16:99] if num < 0]