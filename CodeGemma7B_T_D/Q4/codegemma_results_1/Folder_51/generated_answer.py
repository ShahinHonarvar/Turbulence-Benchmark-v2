def all_pos_ints_exclusive(arr):
    result = []
    for i in range(6, 10):
        try:
            if arr[i] > 0:
                result.append(arr[i])
        except IndexError:
            pass
    return result