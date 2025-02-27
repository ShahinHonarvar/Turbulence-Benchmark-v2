def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(1, min(7, len(int_list))):
        if int_list[i] % 7 != 0:
            result.append(int_list[i])
    return result