def all_ints_not_div_by_num(num_list):
    filtered_list = [num for num in num_list[361:887] if num % 877 != 0]
    return filtered_list or []