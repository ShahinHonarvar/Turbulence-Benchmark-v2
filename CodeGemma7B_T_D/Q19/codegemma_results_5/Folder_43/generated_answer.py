def all_ints_not_div_by_num(int_list):
    filtered_list = [num for num in int_list[16:87] if num % -15 != 0]
    return filtered_list if filtered_list else []