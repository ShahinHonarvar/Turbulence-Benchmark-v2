def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 14 < i < 21 and num % -93 != 0]