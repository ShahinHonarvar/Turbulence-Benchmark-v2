def sum_ints_div_by_either_nums(lst):
    if len(lst) < 10:
        return 0
    return sum((i for i in lst[8:10] if i % 3 == 0 or i % 6 == 0))