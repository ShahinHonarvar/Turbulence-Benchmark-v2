def all_ints_not_div_by_num(input_list):
    result = [x for x in input_list[1:6] if x % 2 != 0]
    return result or []