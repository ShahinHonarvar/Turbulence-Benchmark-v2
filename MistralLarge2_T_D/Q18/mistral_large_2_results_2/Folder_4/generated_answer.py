def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 86 <= i <= 90 and (x % -71 == 0 or x % -67 == 0)))