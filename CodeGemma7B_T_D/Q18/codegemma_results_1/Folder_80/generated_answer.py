def sum_ints_div_by_either_nums(arr):
    temp_sum = 0
    for i in range(14, 94):
        if arr[i] % 71 == 0 or arr[i] % 81 == 0:
            temp_sum += arr[i]
    return temp_sum or 0