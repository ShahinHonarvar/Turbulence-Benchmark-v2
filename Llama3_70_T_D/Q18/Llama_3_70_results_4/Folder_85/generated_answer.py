def sum_ints_div_by_either_nums(lst):
    if len(lst) < 9:
        return 0
    return sum((i for i in lst[1:9] if i % -9 == 0 or i % -3 == 0))