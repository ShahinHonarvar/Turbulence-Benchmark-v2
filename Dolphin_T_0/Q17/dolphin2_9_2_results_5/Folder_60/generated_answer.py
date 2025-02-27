def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(10, 80):
        if i in lst and i % -74 == 0 and (i % -58 == 0):
            result.append(i)
    return result