def all_neg_ints_inclusive(arr):
    res = []
    for i in range(len(arr)):
        if arr[i] < 0:
            res.append(arr[i])
    return res