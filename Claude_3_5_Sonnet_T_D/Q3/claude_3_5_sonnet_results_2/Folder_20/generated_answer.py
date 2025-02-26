def all_pos_ints_inclusive(integer_list):
    start_index = 56
    end_index = 67
    if len(integer_list) <= start_index:
        return []
    subset = integer_list[start_index:end_index]
    return [num for num in subset if num > 0]