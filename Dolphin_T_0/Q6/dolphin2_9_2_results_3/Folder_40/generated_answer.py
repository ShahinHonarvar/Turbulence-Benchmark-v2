def all_neg_ints_exclusive(arr):
    negatives = [i for i in arr[1:-1] if i < 0]
    return negatives