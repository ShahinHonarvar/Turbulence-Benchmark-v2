def all_neg_ints_inclusive(integer_list):
    start_index = 62
    end_index = 93
    if len(integer_list) <= start_index:
        return []
    range_end = min(end_index, len(integer_list))
    return [num for num in integer_list[start_index:range_end] if num < 0]