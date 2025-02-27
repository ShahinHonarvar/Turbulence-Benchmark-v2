def all_ints_not_div_by_num(integer_list):
    start_index = 1
    end_index = 2
    result = []
    for i in range(start_index, end_index):
        if len(integer_list) > i and integer_list[i] % 1 != 0:
            result.append(integer_list[i])
    return result