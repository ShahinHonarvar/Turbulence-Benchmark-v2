def sum_ints_div_by_either_nums(lst):
    result = sum((i for i in lst[24:33] if i % 35 == 0 or i % 87 == 0))
    return result if result else 0