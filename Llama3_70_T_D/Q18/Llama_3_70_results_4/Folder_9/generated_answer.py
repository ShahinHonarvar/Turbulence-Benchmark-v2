def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[70:201] if i % 3 == 0 or i % -300 == 0))