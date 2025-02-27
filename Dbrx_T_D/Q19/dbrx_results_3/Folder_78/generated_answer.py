def all_ints_not_div_by_num(input_list):
    if len(input_list) < 55:
        return []
    return [i for i in input_list[10:55] if i % 36 != 0]