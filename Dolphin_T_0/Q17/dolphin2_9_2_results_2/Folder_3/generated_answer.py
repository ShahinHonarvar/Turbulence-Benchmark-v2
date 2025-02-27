def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(38, 53):
        if i in lst and i % -41 == 0 and (i % -47 == 0):
            result.append(i)
    return result