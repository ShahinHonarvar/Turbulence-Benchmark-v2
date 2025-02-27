def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(29, 54):
        if i in lst and i % -68 == 0 and (i % -85 == 0):
            result.append(i)
    return result