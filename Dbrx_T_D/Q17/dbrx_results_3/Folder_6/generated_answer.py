def all_ints_div_by_both_two_nums(input_list):
    output_list = [input_list[i] for i in range(41, 57) if input_list[i] % 82 == 0 and input_list[i] % 90 == 0]
    return output_list