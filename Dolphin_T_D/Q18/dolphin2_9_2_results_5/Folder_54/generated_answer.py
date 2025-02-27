def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(13, 92):
        if arr[i] % -65 == 0 or arr[i] % -62 == 0:
            total += arr[i]
    return total if total != 0 else 0