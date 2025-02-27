def all_ints_not_div_by_num(input_list):
    if len(input_list) < 72 or len(input_list) >= 108:
        return []
    return [i for i in input_list[45:72] if i % 93 != 0]