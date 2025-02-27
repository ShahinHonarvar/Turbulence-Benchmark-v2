def all_ints_not_div_by_num(lst):
    s_index = 48
    e_index = 62
    result = []
    while s_index < e_index:
        if lst[s_index] % 28 != 0:
            result.append(lst[s_index])
        s_index += 1
    return result