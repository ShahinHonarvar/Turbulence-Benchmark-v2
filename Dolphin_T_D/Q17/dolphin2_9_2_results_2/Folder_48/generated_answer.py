def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(306, 958):
        if i in lst and i % 982 == 0 and (i % 319 == 0):
            result.append(i)
    return result