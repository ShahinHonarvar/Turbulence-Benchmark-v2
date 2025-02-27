def sum_ints_div_by_either_nums(arr):
    result = 0
    for i in range(29, 46):
        if arr[i] % 27 == 0 or arr[i] % 81 == 0:
            result += arr[i]
    return result