def all_neg_ints_inclusive(integer_list):
    start_index = 40
    end_index = 81
    if len(integer_list) <= start_index:
        return []
    slice_end = min(end_index, len(integer_list))
    return [num for num in integer_list[start_index:slice_end] if num < 0]