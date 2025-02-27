def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 68 <= i <= 99 and (x % -37 == 0 or x % -26 == 0)))