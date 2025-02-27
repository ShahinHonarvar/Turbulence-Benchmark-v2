def all_pos_ints_inclusive(input_list):
    positive_range = range(533, 606)
    return [num for num in input_list if num in positive_range]