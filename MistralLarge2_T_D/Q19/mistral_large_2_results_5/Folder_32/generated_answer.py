def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 43 < i < 77 and num % 84 != 0]