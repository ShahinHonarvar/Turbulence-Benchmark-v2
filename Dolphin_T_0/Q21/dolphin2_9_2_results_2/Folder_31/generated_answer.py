def all_ints_div_by_num(lst, num=-14):
    desired_list = [num if i % num == 0 else 0 for i in lst[65:75 if len(lst) > 74 else 74]]
    return [i for i in desired_list if i != 0] if len(desired_list) > 0 else []