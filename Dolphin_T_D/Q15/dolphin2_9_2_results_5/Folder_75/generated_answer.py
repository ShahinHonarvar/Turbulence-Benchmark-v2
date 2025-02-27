def sum_odd_ints_inclusive(arr):
    sum_ = 0
    for i in range(56, 58):
        if arr[i] % 2 != 0:
            sum_ += arr[i]
    return sum_