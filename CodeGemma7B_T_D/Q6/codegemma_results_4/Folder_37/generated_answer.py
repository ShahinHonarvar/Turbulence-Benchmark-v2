def all_neg_ints_exclusive(arr):
    result = []
    for i in range(1, 2):
        if arr[i] < 0:
            result.append(arr[i])
    if not result:
        return []
    return result