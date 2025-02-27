def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in lst[58:76]:
        if i % 72 == 0 or i % 62 == 0:
            s += i
    return s if s != 0 else 0