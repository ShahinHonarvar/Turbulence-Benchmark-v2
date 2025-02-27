def all_ints_not_div_by_num(lst):
    return [elem for elem in lst[70:200] if elem % 300 != 0] if lst else []