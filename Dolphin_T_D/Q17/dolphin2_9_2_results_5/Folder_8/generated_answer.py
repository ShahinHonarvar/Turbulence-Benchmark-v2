def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(36, 86):
        if i in lst and i % -27 == 0 and (i % -96 == 0):
            result.append(i)
    return result