def all_ints_div_by_both_two_nums(lst):
    res = []
    for i in range(8, 10):
        if lst[i] % -3 == 0 and lst[i] % 6 == 0:
            res.append(lst[i])
    return res