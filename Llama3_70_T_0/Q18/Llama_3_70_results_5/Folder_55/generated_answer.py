def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[:10] if i % 10 == 0 or i % 100 == 0))