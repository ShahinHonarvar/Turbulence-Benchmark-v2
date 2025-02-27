def all_ints_div_by_num(int_list):
    result = []
    if len(int_list) > 0 and int_list[0] % 4 == 0:
        result.append(int_list[0])
    return result