def all_ints_div_by_num(integer_list):
    if len(integer_list) <= 10:
        return []
    return [integer_list[10]] if integer_list[10] % 1 == 0 else []