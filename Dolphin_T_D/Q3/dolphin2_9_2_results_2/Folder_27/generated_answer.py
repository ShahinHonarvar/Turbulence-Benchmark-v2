def all_pos_ints_inclusive(arr):
    result = []
    for i in range(66, 94):
        if 0 < arr[i] < 10:
            result.append(arr[i])
    return result