def all_pos_ints_exclusive(input_list):
    result = []
    for i in range(3, 8):
        if i in range(len(input_list)) and input_list[i] > 0:
            result.append(input_list[i])
    return result