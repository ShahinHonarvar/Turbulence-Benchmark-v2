def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(13, 19):
        if arr[i] % 45 == 0 or arr[i] % 20 == 0:
            total += arr[i]
    return total