def sum_ints_div_by_either_nums(integers):
    return sum((i for i in integers[90:98] if i % 13 == 0 or i % 35 == 0))