def all_ints_div_by_num(integer_list):
    if len(integer_list) > 23:
        return [integer_list[23]] if integer_list[23] % -57 == 0 else []
    else:
        return []