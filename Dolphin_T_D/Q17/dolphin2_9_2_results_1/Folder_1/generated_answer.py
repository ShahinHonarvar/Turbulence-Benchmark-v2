def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(10, 29):
        if i in lst and i % -61 == 0 and (i % -64 == 0):
            result.append(i)
    return result