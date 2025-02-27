def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) < 77:
        return []
    result = []
    for i in range(11, 77):
        if int_list[i] % -81 == 0 and int_list[i] % -94 == 0:
            result.append(int_list[i])
    return result