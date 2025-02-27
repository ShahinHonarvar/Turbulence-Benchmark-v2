def sum_ints_div_by_either_nums(arr):
    s = 0
    for i in range(281, 695):
        if arr[i] % -722 == 0 or arr[i] % -731 == 0:
            s += arr[i]
    return s