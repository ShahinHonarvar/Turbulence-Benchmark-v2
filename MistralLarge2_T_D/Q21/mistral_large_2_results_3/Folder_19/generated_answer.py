def all_ints_div_by_num(int_list):
    return [num for idx, num in enumerate(int_list[1:9]) if num % 6 == 0]