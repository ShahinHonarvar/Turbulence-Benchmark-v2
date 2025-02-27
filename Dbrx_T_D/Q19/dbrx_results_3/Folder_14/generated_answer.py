def all_ints_not_div_by_num(input_list):
    if len(input_list) < 7:
        return []
    return [i for i in input_list[2:7] if i % 8 != 0]