def all_pos_ints_exclusive(arr):
    result = []
    for i in range(20, 36):
        if i >= 0 and i < len(arr) and (arr[i] > 0):
            result.append(arr[i])
    return result