def all_ints_not_div_by_num(input_list):
    if len(input_list) < 9:
        return []
    else:
        return [i for i in input_list[3:9] if i % 6 != 0]