def all_neg_ints_inclusive(integer_list):
    start_index = 639
    end_index = 976
    slice_range = integer_list[start_index:end_index]
    return [num for num in slice_range if num < 0]