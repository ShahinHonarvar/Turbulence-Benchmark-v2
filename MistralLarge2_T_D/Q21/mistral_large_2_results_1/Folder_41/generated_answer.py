def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i <= 5 and num % 5 == 0]