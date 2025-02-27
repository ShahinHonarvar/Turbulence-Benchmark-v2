def sum_ints_div_by_either_nums(int_list):
    return sum((i for i in int_list[154:799] if i % 275 == 0 or i % 580 == 0))