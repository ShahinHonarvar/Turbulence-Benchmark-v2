def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(54, 80):
        if i in lst and i % 54 == 0 and (i % 28 == 0):
            result.append(i)
    return result