def all_pos_ints_inclusive(int_list):
    start = 62
    end = 93
    return [num for num in int_list[start:end] if num > 0]