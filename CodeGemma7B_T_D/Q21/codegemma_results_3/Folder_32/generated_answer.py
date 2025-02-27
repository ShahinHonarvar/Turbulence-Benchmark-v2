def all_ints_div_by_num(list_of_int):
    filtered_list = [num for num in list_of_int[38:56] if num % 31 == 0]
    return filtered_list or []