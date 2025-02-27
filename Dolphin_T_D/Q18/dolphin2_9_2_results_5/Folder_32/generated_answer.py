def sum_ints_div_by_either_nums(lst):
    result = sum((i for i in lst[25:96] if i % 51 == 0 or i % 77 == 0))
    return result if result else 0