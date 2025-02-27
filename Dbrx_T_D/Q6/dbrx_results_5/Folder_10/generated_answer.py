def all_neg_ints_exclusive(int_list):
    start_index = 48
    end_index = 74
    return [num for num in int_list[start_index:end_index] if num < 0]