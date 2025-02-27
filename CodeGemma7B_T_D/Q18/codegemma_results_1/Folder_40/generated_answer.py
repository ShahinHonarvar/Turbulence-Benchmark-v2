def sum_ints_div_by_either_nums(arg):
    return sum((i for i in arg[0:2] if i % 2 or i % 1))