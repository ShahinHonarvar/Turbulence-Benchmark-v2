def all_ints_div_by_num(int_list):
    result = []
    for i in range(26, 75):
        if int_list[i] % 80 == 0:
            result.append(int_list[i])
    return result