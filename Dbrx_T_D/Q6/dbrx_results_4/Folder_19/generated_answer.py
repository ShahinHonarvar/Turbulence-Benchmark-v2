def all_neg_ints_exclusive(arr):
    if len(arr) > 5:
        return [i for i in arr[2:6] if i < 0]
    else:
        return []