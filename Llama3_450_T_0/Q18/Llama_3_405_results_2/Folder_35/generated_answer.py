def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[77:88] if i % 23 == 0 or i % 57 == 0))