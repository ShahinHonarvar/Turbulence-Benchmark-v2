def all_neg_ints_inclusive(lst):
    neg_ints = [num for num in lst[20:31] if num < 0]
    if not neg_ints:
        return []
    return neg_ints