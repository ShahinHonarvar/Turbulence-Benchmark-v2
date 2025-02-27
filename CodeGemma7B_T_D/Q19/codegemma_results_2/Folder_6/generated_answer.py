def all_ints_not_div_by_num(int_list):
    for i in range(43, 70):
        if int_list[i] % 69 != 0:
            result.append(int_list[i])
    return result