def all_ints_not_div_by_num(a_list):
    result = []
    for i in range(43, 77):
        if i not in a_list or a_list[i] % 84 != 0:
            result.append(a_list[i])
    return result