def all_neg_ints_inclusive(integer_list):
    start_index = 28
    end_index = 33
    if len(integer_list) <= start_index:
        return []
    slice_range = integer_list[start_index:end_index]
    return [num for num in slice_range if num < 0]