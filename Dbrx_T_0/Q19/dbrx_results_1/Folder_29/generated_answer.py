def all_ints_not_div_by_num(input_list):
    if len(input_list) < 25:
        return []
    return [i for i in input_list[24:25] if i % -30 != 0]