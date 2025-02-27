def all_ints_not_div_by_num(int_list):
    new_list = [num for num in int_list[40:200] if num % 71 != 0]
    return new_list or []