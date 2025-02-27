def all_ints_div_by_num(int_list):
    if len(int_list) < 5:
        return []
    result = []
    if int_list[4] % 3 == 0:
        result.append(int_list[4])
    return result