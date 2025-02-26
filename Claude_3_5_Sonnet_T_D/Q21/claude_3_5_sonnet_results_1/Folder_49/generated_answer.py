def all_ints_div_by_num(integer_list):
    start_index = 30
    end_index = 301
    result = []
    for i in range(start_index, min(end_index, len(integer_list))):
        if integer_list[i] % 5 == 0:
            result.append(integer_list[i])
    return result