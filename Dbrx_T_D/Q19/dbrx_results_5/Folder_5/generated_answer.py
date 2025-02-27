def all_ints_not_div_by_num(int_list):
    start_index = 1
    end_index = 2
    target_list = []
    for i in range(start_index, end_index):
        if int_list[i] % 8 != 0:
            target_list.append(int_list[i])
    return target_list