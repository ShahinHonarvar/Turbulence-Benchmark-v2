def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 50 <= i <= 200 and (x % -34 == 0 or x % 64 == 0)))