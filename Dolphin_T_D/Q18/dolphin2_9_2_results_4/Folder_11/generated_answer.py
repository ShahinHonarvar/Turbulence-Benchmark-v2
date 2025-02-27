def sum_ints_div_by_either_nums(arr):
    sum = 0
    for i in range(22, 25):
        if arr[i] % -85 == 0 or arr[i] % -30 == 0:
            sum += arr[i]
    return sum