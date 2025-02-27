def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(77, 88):
        if i in lst and i % 23 == 0 and (i % 57 == 0):
            result.append(i)
    return result