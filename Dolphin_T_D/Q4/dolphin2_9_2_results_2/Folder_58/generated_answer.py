def all_pos_ints_exclusive(arr):
    result = []
    for i in range(276, 376):
        if arr[i] > 0:
            result.append(arr[i])
    if len(result) == 0:
        return []
    return result