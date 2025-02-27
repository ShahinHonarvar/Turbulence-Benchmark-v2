def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[81:90] if i % 56 == 0 or i % 68 == 0)) if len(lst) > 89 else 0