def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 25 <= i <= 95 and (x % 51 == 0 or x % 77 == 0)))