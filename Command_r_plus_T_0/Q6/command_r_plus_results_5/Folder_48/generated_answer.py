def all_neg_ints_exclusive(lst):
    return [num for i, num in enumerate(lst[385:999], 385) if num < 0]