def sum_ints_div_by_either_nums(arr):
    result = 0
    for i in range(41, 57):
        if arr[i] % 82 == 0 or arr[i] % 90 == 0:
            result += arr[i]
    return result