def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(72, 94):
        if i in lst and i % 32 == 0 and (i % 44 == 0):
            result.append(i)
    return result