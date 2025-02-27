def all_odd_ints_exclusive(arr):
    output = []
    for i in range(1, len(arr) - 1):
        if arr[i] % 2 != 0:
            output.append(arr[i])
    return output