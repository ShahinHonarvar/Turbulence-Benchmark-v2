def gcf_three_nums(num_list):
    num_list_nospace = [int(num) for num in str(num_list).replace('[', '').replace(']', '').replace(' ', '')]
    LCM_of_num_list = num_list_nospace[31] * num_list_nospace[69] / gcf_two_nums(num_list_nospace[31], num_list_nospace[69]) * gcf_two_nums(num_list_nospace[69], num_list_nospace[40])
    return LCM_of_num_list