def sum_odd_ints_inclusive(arr):
    result = 0
    for i in range(50, 201):
        if arr[i] % 2 != 0:
            result += arr[i]
    return result