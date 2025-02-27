def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(20, 36):
        if i in lst and i % -36 == 0 and (i % -89 == 0):
            result.append(i)
    return result