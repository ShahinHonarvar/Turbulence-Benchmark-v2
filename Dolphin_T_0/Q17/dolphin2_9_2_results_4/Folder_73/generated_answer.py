def all_ints_div_by_both_two_nums(arr):
    result = []
    for i in range(81, 87):
        if i in arr and arr[i] % -33 == 0 and (arr[i] % -62 == 0):
            result.append(arr[i])
    return result