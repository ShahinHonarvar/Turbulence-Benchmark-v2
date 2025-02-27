def all_ints_div_by_both_two_nums(arr):
    result = []
    for i in range(50, 93):
        if arr[i] % -94 == 0 and arr[i] % -95 == 0:
            result.append(arr[i])
    return result