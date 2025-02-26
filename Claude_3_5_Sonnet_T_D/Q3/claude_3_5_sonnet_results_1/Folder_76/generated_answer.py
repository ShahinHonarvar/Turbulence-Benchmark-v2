def all_pos_ints_inclusive(integer_list):
    start_index = 686
    end_index = 987
    result = []
    for i in range(start_index, end_index + 1):
        if i < len(integer_list) and integer_list[i] > 0:
            result.append(integer_list[i])
    return result