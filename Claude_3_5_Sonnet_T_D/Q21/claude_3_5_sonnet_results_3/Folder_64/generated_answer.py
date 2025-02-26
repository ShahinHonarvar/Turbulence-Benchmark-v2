def all_ints_div_by_num(int_list):
    result = []
    if int_list and int_list[0] % 4 == 0:
        result.append(int_list[0])
    return result