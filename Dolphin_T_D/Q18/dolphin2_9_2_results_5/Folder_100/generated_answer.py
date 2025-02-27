def sum_ints_div_by_either_nums(arr):
    s = 0
    for i in range(72, 94):
        if arr[i] % 32 == 0 or arr[i] % 44 == 0:
            s += arr[i]
    return s