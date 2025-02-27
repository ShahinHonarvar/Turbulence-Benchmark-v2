def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(42, 88):
        if i in lst and i % -90 == 0 and (i % -74 == 0):
            result.append(i)
    return result