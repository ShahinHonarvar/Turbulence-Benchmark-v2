def all_neg_ints_inclusive(arr):
    neg_ints = [n for n in arr[3:6] if n < 0]
    if not neg_ints:
        return []
    return neg_ints