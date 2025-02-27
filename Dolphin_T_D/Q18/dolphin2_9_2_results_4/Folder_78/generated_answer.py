def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(34, 70):
        if i >= len(arr):
            break
        if arr[i] % 19 == 0 or arr[i] % 32 == 0:
            total += arr[i]
    return total