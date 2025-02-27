def all_ints_not_div_by_num(integer_list):
    result = [x for x in integer_list[12:56] if x % 90 != 0]
    return result