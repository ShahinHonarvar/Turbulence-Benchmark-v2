def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(306, 958):
        if i < len(lst):
            if lst[i] % 982 == 0 or lst[i] % 319 == 0:
                result += lst[i]
    return result