def all_ints_not_div_by_num(input_list):
    return [x for i, x in enumerate(input_list[31:70]) if x % -70 != 0]