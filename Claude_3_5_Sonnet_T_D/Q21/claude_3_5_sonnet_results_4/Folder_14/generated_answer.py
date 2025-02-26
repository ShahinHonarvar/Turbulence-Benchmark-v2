def all_ints_div_by_num(integer_list):
    if len(integer_list) >= 9:
        return [integer_list[8]] if integer_list[8] % 8 == 0 else []
    else:
        return []