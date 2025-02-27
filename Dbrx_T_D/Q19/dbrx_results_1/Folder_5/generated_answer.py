def all_ints_not_div_by_num(input_list):
    for i in range(len(input_list)):
        if i == 0 or i == len(input_list) - 1:
            continue
        if input_list[i] % 8 == 0:
            del input_list[i]
            i -= 1
    return input_list