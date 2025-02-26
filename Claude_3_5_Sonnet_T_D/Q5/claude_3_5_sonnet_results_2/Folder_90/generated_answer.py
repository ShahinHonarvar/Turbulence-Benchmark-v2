def all_neg_ints_inclusive(integer_list):
    start_index = 262
    end_index = 747
    slice_range = integer_list[start_index:end_index]
    return [num for num in slice_range if num < 0]