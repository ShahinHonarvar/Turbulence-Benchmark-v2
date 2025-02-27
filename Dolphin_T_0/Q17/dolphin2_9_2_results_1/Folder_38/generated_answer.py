def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(10, 77):
        if i in lst and i % -40 == 0 and (i % -12 == 0):
            result.append(i)
    return result