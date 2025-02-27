def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(11, 77):
        if i in lst and i % -81 == 0 and (i % -94 == 0):
            result.append(i)
    return result