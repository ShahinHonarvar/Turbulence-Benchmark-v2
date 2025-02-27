def sum_ints_div_by_either_nums(lst):
    if len(lst) < 7:
        lst = lst + [0] * (7 - len(lst))
    return sum((i for i in lst[:7] if i % -5 == 0 or i % -6 == 0))