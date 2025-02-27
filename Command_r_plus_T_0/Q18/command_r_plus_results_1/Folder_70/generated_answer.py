def sum_ints_div_by_either_nums(lst):
    if 42 < len(lst) - 1:
        return sum((i for i in lst[42:44] if i % 15 == 0 or i % 87 == 0))
    else:
        return 0