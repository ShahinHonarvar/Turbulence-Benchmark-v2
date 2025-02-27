def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(58, 82):
        if i in lst and i % 55 == 0 and (i % 10 == 0):
            result.append(i)
    return result