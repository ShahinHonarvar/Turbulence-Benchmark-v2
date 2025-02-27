def all_neg_ints_exclusive(arr):
    result = []
    for i in range(9, 11):
        if arr[i] < 0:
            result.append(arr[i])
    return result