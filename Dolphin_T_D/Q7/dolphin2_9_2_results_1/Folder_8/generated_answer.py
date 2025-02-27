def all_even_ints_inclusive(arr):
    result = []
    for i in range(23, 24):
        if arr[i] % 2 == 0:
            result.append(arr[i])
    return result