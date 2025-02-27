def all_ints_not_div_by_num(int_list):
    start_index = 1
    end_index = 2
    result = []
    for i in range(len(int_list)):
        if i >= start_index and i < end_index and (int_list[i] % 5 != 0):
            result.append(int_list[i])
    return result