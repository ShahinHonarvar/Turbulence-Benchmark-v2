def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[90:201] if i % -31 == 0 or i % 13 == 0))