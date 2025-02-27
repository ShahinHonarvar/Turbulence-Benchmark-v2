def all_neg_ints_inclusive(arr):
    result = [x for x in arr[5:8] if x < 0]
    return result if len(result) > 0 else []