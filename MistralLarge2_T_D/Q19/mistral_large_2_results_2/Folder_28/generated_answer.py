def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 81 < i < 86 and num % 77 != 0]