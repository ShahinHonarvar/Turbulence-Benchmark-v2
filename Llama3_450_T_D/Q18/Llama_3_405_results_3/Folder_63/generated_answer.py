def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[31:51] if i % 81 == 0 or i % 64 == 0))