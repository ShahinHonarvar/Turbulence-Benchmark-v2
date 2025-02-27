def all_ints_div_by_both_two_nums(arr):
    result = []
    for num in arr[10:76]:
        if num % -81 == 0 and num % -94 == 0:
            result.append(num)
    return result