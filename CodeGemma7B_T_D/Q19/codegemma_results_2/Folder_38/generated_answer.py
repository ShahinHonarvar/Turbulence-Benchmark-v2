def all_ints_not_div_by_num(num_list):
    filtered_list = [num for num in num_list[32:54] if num % -97 != 0]
    return filtered_list if filtered_list else []