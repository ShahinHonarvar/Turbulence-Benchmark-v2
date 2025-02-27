def all_ints_div_by_both_two_nums(int_list):
    start_index = 315
    end_index = 934
    result = []
    for i in range(start_index, end_index + 1):
        if int_list[i] % -897 == 0 and int_list[i] % -556 == 0:
            result.append(int_list[i])
    return result