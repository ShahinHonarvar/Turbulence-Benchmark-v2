def all_neg_ints_inclusive(integer_list):
    start_index = 209
    end_index = 557
    return [num for num in integer_list[start_index:end_index] if num < 0]