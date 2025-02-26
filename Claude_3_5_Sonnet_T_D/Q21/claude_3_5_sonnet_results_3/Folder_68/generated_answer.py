def all_ints_div_by_num(integer_list):
    if not integer_list:
        return []
    return [integer_list[0]] if integer_list[0] % 8 == 0 else []