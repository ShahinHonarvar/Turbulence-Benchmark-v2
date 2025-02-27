def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 48 < i < 92 and num % 90 != 0]