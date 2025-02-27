def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(57, 86):
        if i in lst:
            if lst[i] % -77 == 0 or lst[i] % -32 == 0:
                result += lst[i]
    return result