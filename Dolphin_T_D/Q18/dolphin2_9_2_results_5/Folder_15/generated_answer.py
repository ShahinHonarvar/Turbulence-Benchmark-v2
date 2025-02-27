def sum_ints_div_by_either_nums(lst):
    s = 0
    for i in lst[:3]:
        if i % -2 == 0 or i % 3 == 0:
            s += i
    return s