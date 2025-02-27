def sum_ints_div_by_either_nums(integers):
    return sum((i for i in integers[25:81] if i % -20 == 0 or i % -26 == 0))