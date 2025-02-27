def sum_odd_ints_inclusive(arr):
    sum = 0
    for i in range(533, 606):
        if arr[i] % 2 == 1:
            sum += arr[i]
    return sum