def all_even_ints_exclusive(arr):
    result = []
    for i in range(1, len(arr) - 1):
        if arr[i] % 2 == 0:
            result.append(arr[i])
    return result