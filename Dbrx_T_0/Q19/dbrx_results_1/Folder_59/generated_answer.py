def all_ints_not_div_by_num(input_list):
    if len(input_list) < 10:
        return []
    return [i for i in input_list[8:9] if i % 8 != 0]