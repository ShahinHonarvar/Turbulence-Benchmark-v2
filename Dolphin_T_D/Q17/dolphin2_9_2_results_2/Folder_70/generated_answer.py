def all_ints_div_by_both_two_nums(lst):
    res = []
    for i in range(42, 44):
        if i in lst and i % 15 == 0 and (i % 87 == 0):
            res.append(i)
    return res