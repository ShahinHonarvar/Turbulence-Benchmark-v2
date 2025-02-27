def all_neg_ints_exclusive(arr):
    return [x for i, x in enumerate(arr[56:88]) if i > 0 and i < len(arr) - 1 and (x < 0)]