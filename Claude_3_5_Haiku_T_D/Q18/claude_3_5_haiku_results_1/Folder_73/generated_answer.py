def sum_ints_div_by_either_nums(arr):
    total = 0
    for num in arr[81:87]:
        if num % -33 == 0 or num % -62 == 0:
            total += num
    return total