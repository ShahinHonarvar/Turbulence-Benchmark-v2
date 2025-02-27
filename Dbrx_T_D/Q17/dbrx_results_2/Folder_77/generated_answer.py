def all_ints_div_by_both_two_nums(int_list):
    start_index = 828
    end_index = 932
    div_649_461 = []
    for i in range(start_index, end_index + 1):
        if len(int_list) > i and int_list[i] % -649 == 0 and (int_list[i] % -461 == 0):
            div_649_461.append(int_list[i])
    return div_649_461