def all_ints_not_div_by_num(lst):
    range_list = lst[2:9]
    not_divisible_by_minus_6 = [i for i in range_list if i % -6 != 0]
    if not_divisible_by_minus_6:
        return not_divisible_by_minus_6
    else:
        return []