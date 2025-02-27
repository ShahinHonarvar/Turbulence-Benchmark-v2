def sum_ints_div_by_either_nums(ints_list):
    return sum((x for i, x in enumerate(ints_list) if 73 <= i <= 86 and (x % 54 == 0 or x % 82 == 0)))