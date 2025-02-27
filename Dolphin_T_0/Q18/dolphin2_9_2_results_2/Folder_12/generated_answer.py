def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(35, 65):
        if i in lst:
            if lst[i] % -30 == 0 or lst[i] % -95 == 0:
                result += lst[i]
    return result