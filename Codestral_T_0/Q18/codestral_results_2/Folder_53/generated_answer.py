def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[200:201] if i % 17 == 0 or i % -5 == 0))