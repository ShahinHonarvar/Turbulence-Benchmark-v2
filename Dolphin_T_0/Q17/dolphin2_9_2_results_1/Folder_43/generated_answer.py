def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(57, 86):
        if i in lst and i % -77 == 0 and (i % -32 == 0):
            result.append(i)
    return result