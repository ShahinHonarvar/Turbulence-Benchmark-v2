def all_ints_div_by_num(int_list):
    result = []
    for i in range(min(6, len(int_list))):
        if int_list[i] % 6 == 0:
            result.append(int_list[i])
    return result