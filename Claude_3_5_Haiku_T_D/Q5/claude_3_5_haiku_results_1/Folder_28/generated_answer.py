def all_neg_ints_inclusive(lst):
    if len(lst) < 64:
        return []
    slice_range = lst[62:64]
    return [x for x in slice_range if x < 0]