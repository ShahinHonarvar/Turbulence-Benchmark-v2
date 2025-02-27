def sum_ints_div_by_either_nums(arr):
    total = 0
    for i in arr[86:90]:
        if i % -61 == 0 or i % -79 == 0:
            total += i
    return total if total != 0 else None