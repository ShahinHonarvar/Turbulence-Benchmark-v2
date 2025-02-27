def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 51 <= i <= 76 and (x % -90 == 0 or x % -59 == 0)))