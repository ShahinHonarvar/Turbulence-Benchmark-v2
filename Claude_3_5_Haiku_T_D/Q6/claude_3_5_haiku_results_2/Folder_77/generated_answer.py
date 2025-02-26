def all_neg_ints_exclusive(lst):
    if len(lst) <= 111 or len(lst) <= 473:
        return []
    return [num for num in lst[112:473] if num < 0]