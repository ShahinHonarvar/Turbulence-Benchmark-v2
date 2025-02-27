def sum_ints_div_by_either_nums(lst):
    if len(lst) < 11:
        return 0
    return sum((i for i in lst[10:77] if i % -40 == 0 or i % -12 == 0))