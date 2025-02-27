def all_ints_not_div_by_num(input_list):
    if len(input_list) < 20:
        return []
    return [i for i in input_list[15:20] if i % 93 != 0]