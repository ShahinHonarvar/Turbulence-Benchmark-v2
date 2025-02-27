def all_neg_ints_inclusive(arr):
    if len(arr) == 0:
        return []
    elif arr[0] < 0:
        return [i for i in arr if i <= 0]
    else:
        return []