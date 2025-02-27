def sum_ints_div_by_either_nums(arr):
    result = 0
    for i in range(35, 65):
        if arr[i] % -30 == 0 or arr[i] % -95 == 0:
            result += arr[i]
    return result