def all_ints_div_by_num(integer_list):
    start_index = 319
    end_index = 612
    result = []
    for i in range(start_index, end_index + 1):
        if integer_list[i] % -215 == 0:
            result.append(integer_list[i])
    return result