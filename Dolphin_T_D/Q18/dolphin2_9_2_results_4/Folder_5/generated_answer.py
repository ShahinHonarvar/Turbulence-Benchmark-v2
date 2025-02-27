def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(2):
        if i % -6 == 0 or i % 4 == 0:
            s += lst[i]
    return s