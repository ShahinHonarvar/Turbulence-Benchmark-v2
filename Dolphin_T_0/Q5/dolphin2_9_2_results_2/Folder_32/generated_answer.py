def all_neg_ints_inclusive(arr):
    result = []
    for i in range(21, 98):
        if arr[i] < 0:
            result.append(arr[i])
    return result