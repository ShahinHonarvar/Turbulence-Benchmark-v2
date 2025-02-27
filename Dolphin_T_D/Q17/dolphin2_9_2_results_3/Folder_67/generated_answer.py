def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(24, 33):
        if i in lst and i % 35 == 0 and (i % 87 == 0):
            result.append(i)
    return result