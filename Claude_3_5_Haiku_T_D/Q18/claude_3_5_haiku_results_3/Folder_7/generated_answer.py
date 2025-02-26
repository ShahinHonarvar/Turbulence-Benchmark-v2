def sum_ints_div_by_either_nums(arr):
    total_sum = 0
    for i in range(543, 585):
        if i < len(arr):
            if arr[i] % -553 == 0 or arr[i] % -737 == 0:
                total_sum += arr[i]
    return total_sum