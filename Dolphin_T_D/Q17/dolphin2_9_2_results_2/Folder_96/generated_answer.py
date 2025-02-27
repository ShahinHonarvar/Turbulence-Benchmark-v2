def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(50, 201):
        if i in lst and i % -34 == 0 and (i % 64 == 0):
            result.append(i)
    return result