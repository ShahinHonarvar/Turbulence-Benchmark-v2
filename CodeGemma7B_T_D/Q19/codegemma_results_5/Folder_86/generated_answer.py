def all_ints_not_div_by_num(num_list):
    filtered_list = [num for num in num_list[15:63] if num % 34 != 0]
    return filtered_list if filtered_list else []