def all_pos_ints_inclusive(integer_list):
    start_index = 26
    end_index = 53
    result = [num for num in integer_list[start_index:end_index] if num > 0]
    return result