def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(32, 100):
        if i in lst and i % -11 == 0 and (i % -15 == 0):
            result.append(i)
    return result