def all_ints_div_by_both_two_nums(int_list):
    start_index = 828
    end_index = 932
    result = []
    for i in range(start_index, end_index + 1):
        if int_list[i] % -649 == 0 and int_list[i] % -461 == 0:
            result.append(int_list[i])
    return result