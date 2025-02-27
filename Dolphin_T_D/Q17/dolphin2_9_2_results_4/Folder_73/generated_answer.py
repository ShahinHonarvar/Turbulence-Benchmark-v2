def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(81, 87):
        if i in lst and i % -33 == 0 and (i % -62 == 0):
            result.append(i)
    return result