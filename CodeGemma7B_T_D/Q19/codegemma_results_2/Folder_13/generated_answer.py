def all_ints_not_div_by_num(lst):
    filtered_lst = [num for num in lst[32:44] if num % 34 != 0]
    return filtered_lst if filtered_lst else []