def sum_odd_ints_inclusive(arr):
    sum_ = 0
    for i in range(31, 35):
        if arr[i] % 2 != 0:
            sum_ += arr[i]
    return sum_