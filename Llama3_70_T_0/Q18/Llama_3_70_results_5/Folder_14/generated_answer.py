def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[7:10] if i % 2 == 0 or i % 3 == 0))