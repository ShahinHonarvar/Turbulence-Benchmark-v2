def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(86, 90):
        if arr[i] % -61 == 0 or arr[i] % -79 == 0:
            total += arr[i]
    return total