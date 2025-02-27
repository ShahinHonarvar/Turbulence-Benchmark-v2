def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in range(315, 935):
        if i in lst:
            if i % -897 == 0 or i % -556 == 0:
                s += i
    return s