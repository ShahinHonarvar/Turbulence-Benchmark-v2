def sum_ints_div_by_either_nums(lst):
    if len(lst) < 88:
        return 0
    return sum((i for i in lst[77:88] if i % 23 == 0 or i % 57 == 0))