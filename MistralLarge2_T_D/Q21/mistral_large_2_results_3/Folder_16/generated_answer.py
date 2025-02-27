def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 13 <= i <= 68 and num % 71 == 0]