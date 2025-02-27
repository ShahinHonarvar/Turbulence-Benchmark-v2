def all_ints_not_div_by_num(input_list):
    if len(input_list) < 5:
        return []
    return [i for i in input_list[4:5] if i % -7 != 0]