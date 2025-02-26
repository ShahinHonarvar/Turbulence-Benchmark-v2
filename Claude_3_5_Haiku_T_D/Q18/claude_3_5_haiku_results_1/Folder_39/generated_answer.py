def sum_ints_div_by_either_nums(arr):
    if len(arr) <= 76:
        return 0
    total = 0
    for num in arr[13:77]:
        if num % -66 == 0 or num % -32 == 0:
            total += num
    return total