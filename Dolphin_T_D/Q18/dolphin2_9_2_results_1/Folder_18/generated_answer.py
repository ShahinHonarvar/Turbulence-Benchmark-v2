def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in range(55, 67):
        if i in arr and (arr[i] % 22 == 0 or arr[i] % 82 == 0):
            total += arr[i]
    return total