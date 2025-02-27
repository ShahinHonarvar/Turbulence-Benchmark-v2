def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(0, 4):
        if lst[i] % 11 == 0 or lst[i] % -7 == 0:
            result += lst[i]
    return result if result != 0 else 0