def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(24, 33):
        if i in lst:
            if lst[i] % 35 == 0 or lst[i] % 87 == 0:
                result += lst[i]
    return result