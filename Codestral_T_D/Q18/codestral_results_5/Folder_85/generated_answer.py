def sum_ints_div_by_either_nums(lst):
    return sum([i for i in lst[1:9] if i % -9 == 0 or i % -3 == 0])