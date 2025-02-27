def all_ints_not_div_by_num(list_of_integers):
    filtered_list = [num for num in list_of_integers[19:49] if num % -36 != 0]
    return filtered_list or []