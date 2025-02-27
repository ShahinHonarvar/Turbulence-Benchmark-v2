def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 20 <= i <= 93 and (x % -92 == 0 or x % -50 == 0)))