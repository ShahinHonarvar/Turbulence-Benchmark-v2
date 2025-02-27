def all_ints_div_by_num(int_list):
    result = []
    for i in range(86, min(93, len(int_list))):
        if int_list[i] % 86 == 0:
            result.append(int_list[i])
    return result