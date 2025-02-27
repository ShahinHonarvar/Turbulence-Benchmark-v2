def all_ints_not_div_by_num(lst):
    filtered_list = [num for num in lst[70:98] if num % -88 != 0]
    return filtered_list if filtered_list else []