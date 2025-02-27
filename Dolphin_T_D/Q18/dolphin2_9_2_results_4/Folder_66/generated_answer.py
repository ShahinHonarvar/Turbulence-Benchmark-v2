def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(58, 82):
        if arr[i] % 55 == 0 or arr[i] % 10 == 0:
            total += arr[i]
    return total if total != 0 else 0