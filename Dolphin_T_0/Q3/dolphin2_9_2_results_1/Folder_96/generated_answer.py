def all_pos_ints_inclusive(arr):
    result = []
    for i in range(50, 201):
        if arr[i] > 0:
            result.append(arr[i])
    return result