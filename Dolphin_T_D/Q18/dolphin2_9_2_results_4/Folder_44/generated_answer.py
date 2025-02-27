def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(25, 71):
        if arr[i] % 74 == 0 or arr[i] % 15 == 0:
            total += arr[i]
    return total