def all_odd_ints_inclusive(arr):
    result = []
    for i in range(6, 6 + 1):
        if i in range(3, len(arr), 2):
            result.append(arr[i])
    return result