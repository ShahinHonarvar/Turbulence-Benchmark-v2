def all_ints_div_by_both_two_nums(input_list):
    output_list = []
    for i in range(78, 82):
        if i < len(input_list):
            if input_list[i] % 76 == 0 and input_list[i] % 60 == 0:
                output_list.append(input_list[i])
    return output_list