def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(1, 9):
        if i in lst and i % -9 == 0 and (i % -3 == 0):
            result.append(i)
    return result