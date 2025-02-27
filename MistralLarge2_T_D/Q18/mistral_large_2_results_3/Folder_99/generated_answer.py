def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[154:799] if x % 275 == 0 or x % 580 == 0))