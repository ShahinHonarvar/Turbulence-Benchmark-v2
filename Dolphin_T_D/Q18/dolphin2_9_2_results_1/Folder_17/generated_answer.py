def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(81, 90):
        if arr[i] % 56 == 0 or arr[i] % 68 == 0:
            total += arr[i]
    return total