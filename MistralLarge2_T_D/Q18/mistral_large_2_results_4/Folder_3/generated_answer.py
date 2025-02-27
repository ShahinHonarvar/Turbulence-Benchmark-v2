def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 38 <= i <= 52 and (x % -41 == 0 or x % -47 == 0)))