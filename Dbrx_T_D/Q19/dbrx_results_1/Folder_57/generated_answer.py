def all_ints_not_div_by_num(int_list):
    start_index = 56
    end_index = 88
    result = []
    for i in range(start_index, end_index):
        if int_list[i] % -59 != 0:
            result.append(int_list[i])
    return result