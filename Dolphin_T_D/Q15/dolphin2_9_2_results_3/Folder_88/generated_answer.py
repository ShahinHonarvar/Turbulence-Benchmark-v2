def sum_odd_ints_inclusive(arr):
    odd_sum = 0
    for i in range(4, 9):
        if arr[i] % 2 != 0:
            odd_sum += arr[i]
    return odd_sum