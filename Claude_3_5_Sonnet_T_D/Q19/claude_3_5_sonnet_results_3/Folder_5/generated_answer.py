def all_ints_not_div_by_num(int_list):
    return [num for num in int_list[1:-1] if num % 8 != 0]