def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(154, 799):
        if i in lst and i % 275 == 0 and (i % 580 == 0):
            result.append(i)
    return result