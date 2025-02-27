def sum_ints_div_by_either_nums(arr):
    sum = 0
    for i in range(36, 86):
        if arr[i] % -27 == 0 or arr[i] % -96 == 0:
            sum += arr[i]
    return sum