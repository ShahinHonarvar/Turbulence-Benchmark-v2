def all_odd_ints_inclusive(arr):
    result = []
    for i in range(4, 9):
        if arr[i] % 2 != 0:
            result.append(arr[i])
    return result