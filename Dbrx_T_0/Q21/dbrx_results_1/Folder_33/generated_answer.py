def all_ints_div_by_num(int_list):
    start_index = 319
    end_index = 612
    result = []
    for i in range(len(int_list)):
        if i >= start_index and i <= end_index and (int_list[i] % -215 == 0):
            result.append(int_list[i])
    return result