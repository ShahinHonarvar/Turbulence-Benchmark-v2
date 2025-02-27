def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 20 <= i <= 68 and num % 97 != 0]