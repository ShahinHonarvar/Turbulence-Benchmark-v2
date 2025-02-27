def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(10, 77):
        if arr[i] % -40 == 0 or arr[i] % -12 == 0:
            total += arr[i]
    return total