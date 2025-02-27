def sum_ints_div_by_either_nums(data_list):
    total = 0
    for i in range(55, 81):
        if i < len(data_list):
            if data_list[i] % 22 == 0 or data_list[i] % 32 == 0:
                total += data_list[i]
    return total