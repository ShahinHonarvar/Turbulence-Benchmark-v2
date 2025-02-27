def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(48, 77):
        if i in lst and i % 46 == 0 and (i % 82 == 0):
            result.append(i)
    return result