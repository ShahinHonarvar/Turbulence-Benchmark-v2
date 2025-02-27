def sum_odd_ints_inclusive(arr):
    total = 0
    for i in range(43, 87):
        if arr[i] % 2 != 0:
            total += arr[i]
    return total