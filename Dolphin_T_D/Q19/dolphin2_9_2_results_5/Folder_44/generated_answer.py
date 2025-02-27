def all_ints_not_div_by_num(lst_integers):
    filtered_lst = [n for n in lst_integers[46:91] if n % 67 != 0]
    return filtered_lst if filtered_lst else []