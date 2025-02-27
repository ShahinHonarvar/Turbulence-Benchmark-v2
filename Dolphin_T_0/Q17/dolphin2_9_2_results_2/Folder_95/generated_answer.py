def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(57, 85):
        if i in lst and i % -30 == 0 and (i % -88 == 0):
            result.append(i)
    return result