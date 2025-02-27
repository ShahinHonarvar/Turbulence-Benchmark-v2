def all_ints_not_div_by_num(int_list):
    start_index = 62
    end_index = 96
    not_divisible = []
    for i in range(start_index, end_index):
        if int_list[i] % 26 != 0:
            not_divisible.append(int_list[i])
    return not_divisible