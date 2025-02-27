import math

def all_ints_not_div_by_num(list):
    temp_list = list[15:50]
    return [x for x in temp_list if x % 34 != 0]