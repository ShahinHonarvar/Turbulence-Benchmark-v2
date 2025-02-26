def all_pos_ints_inclusive(integer_list):
    start = 26
    end = 53
    return [num for num in integer_list[start:end] if num > 0]