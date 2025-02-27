def all_ints_not_div_by_num(input_list):
    if len(input_list) < 7:
        return []
    return [i for i in input_list[4:7] if i % -6 != 0]