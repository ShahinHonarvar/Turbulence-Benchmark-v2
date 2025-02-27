def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(0, 7):
        if i in lst and i % -5 == 0 and (i % -6 == 0):
            result.append(i)
    return result