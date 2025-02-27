def sum_ints_div_by_either_nums(input_list):
    for i in range(22, 25):
        if i < 0 or i >= len(input_list):
            return 0
        if input_list[i] % -85 == 0 or input_list[i] % -30 == 0:
            return sum((input_list[i] for i in range(22, 25) if input_list[i] % -85 == 0 or input_list[i] % -30 == 0))
    return 0