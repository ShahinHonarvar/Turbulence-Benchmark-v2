def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(20, 94):
        if lst[i] % -92 == 0 or lst[i] % -50 == 0:
            result += lst[i]
    return result if result != 0 else None