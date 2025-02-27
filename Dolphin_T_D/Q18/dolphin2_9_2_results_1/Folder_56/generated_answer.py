def sum_ints_div_by_either_nums(arr):
    s = 0
    for i in range(7, 10):
        if -9 <= arr[i] <= -7 or 9 <= arr[i] <= 7:
            s += arr[i]
    return s