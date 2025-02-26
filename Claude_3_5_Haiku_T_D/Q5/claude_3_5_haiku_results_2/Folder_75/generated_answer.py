def all_neg_ints_inclusive(lst):
    if len(lst) <= 57:
        return []
    slice_range = lst[56:58]
    return [num for num in slice_range if num < 0]