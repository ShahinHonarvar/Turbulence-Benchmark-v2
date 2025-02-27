def all_ints_div_by_both_two_nums(arr):
    result = []
    for i in range(48, 77):
        if arr[i] % -46 == 0 and arr[i] % -82 == 0:
            result.append(arr[i])
    return result