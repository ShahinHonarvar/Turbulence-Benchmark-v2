def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 40 <= i <= 400 and num % 7 == 0]