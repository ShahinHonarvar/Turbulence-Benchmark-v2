def sum_ints_div_by_either_nums(integers):
    return sum((i for i in integers[55:81] if i % 22 == 0 or i % 32 == 0))