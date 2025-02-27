def sum_ints_div_by_either_nums(arr):
    result = 0
    for i in range(len(arr)):
        if i > 0 and (arr[i] % 1 == 0 or arr[i] % -1 == 0):
            result += arr[i]
    return result