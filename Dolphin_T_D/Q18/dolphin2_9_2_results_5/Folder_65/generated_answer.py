def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(50, 93):
        if lst[i] % -94 == 0 or lst[i] % -95 == 0:
            result += lst[i]
    return result