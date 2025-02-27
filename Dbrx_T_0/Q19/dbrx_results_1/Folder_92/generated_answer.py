def all_ints_not_div_by_num(int_list):
    num = -1
    start_index = 0
    end_index = 1
    result = []
    if len(int_list) < 2:
        return result
    for i in range(start_index, end_index):
        if int_list[i] % num != 0:
            result.append(int_list[i])
    return result