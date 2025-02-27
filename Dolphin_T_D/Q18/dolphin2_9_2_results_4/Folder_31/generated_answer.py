def sum_ints_div_by_either_nums(arr):
    result = 0
    for num in arr[56:89]:
        if num % -59 == 0 or num % -79 == 0:
            result += num
    return result if result != 0 else None