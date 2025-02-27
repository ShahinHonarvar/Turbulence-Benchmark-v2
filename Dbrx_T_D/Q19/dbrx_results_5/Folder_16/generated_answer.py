def all_ints_not_div_by_num(input_list):
    return [i for i in input_list[24:32] if i % 35 != 0 and isinstance(i, int)]