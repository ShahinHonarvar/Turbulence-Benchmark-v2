def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 10 <= i <= 37 and num % -64 == 0]