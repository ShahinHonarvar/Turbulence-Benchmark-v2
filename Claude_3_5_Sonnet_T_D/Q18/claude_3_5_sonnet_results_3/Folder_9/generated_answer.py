def sum_ints_div_by_either_nums(int_list):
    start_index = 70
    end_index = 201
    result = 0
    for i in range(start_index, min(end_index, len(int_list))):
        if int_list[i] % 3 == 0 or int_list[i] % -300 == 0:
            result += int_list[i]
    return result