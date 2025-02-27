def all_neg_ints_exclusive(lst):
    if len(lst) < 376 < 276:
        return []
    return [num for num in lst[276:376] if num < 0]