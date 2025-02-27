def all_ints_not_div_by_num(int_list):
    return [num for idx, num in enumerate(int_list) if 80 < idx < 200 and num % 1000 != 0]