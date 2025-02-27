def all_ints_div_by_num(input_list):
    for i in range(len(input_list)):
        if i >= 50 and i <= 54 and (input_list[i] % 84 == 0):
            return [input_list[i]]
    return []