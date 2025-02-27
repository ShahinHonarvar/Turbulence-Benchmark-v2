def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[78:82] if x % 76 == 0 or x % 60 == 0))