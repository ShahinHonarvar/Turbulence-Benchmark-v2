def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(14, 94):
        if lst[i] % 71 == 0 or lst[i] % 81 == 0:
            result += lst[i]
    return result if result != 0 else 0