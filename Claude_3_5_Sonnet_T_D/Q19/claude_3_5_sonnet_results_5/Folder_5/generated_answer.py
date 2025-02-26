def all_ints_not_div_by_num(integer_list):
    return [num for num in integer_list[2:-2] if num % 8 != 0]