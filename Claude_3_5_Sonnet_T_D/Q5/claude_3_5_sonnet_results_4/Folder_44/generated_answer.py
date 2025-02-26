def all_neg_ints_inclusive(integer_list):
    start_index = 13
    end_index = 69
    if len(integer_list) <= start_index:
        return []
    actual_end = min(end_index, len(integer_list))
    return [num for num in integer_list[start_index:actual_end] if num < 0]