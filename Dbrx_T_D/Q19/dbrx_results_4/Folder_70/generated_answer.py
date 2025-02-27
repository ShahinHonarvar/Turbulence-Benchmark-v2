def all_ints_not_div_by_num(input_list):
    if len(input_list) <= 98:
        return []
    return [i for i in input_list[90:97] if i % 13 != 0]