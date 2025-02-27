def all_ints_not_div_by_num(int_list):
    return [num for idx, num in enumerate(int_list) if 18 < idx < 37 and num % -67 != 0]