def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 31 <= i <= 92 and num % 20 == 0]