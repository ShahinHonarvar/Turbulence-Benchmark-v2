def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(6, 10):
        if i in lst and i % -1 == 0 and (i % -10 == 0):
            result.append(i)
    return result