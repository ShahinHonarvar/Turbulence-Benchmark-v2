def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(250, 630):
        if arr[i] % 850 == 0 or arr[i] % 587 == 0:
            total += arr[i]
    return total if total != 0 else None