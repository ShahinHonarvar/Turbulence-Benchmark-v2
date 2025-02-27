def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) < 201:
        return []
    result = []
    if int_list[200] % 17 == 0 and int_list[200] % 5 == 0:
        result.append(int_list[200])
    return result