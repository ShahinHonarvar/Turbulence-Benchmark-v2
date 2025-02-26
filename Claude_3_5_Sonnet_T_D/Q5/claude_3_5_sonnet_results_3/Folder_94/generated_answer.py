def all_neg_ints_inclusive(integer_list):
    start_index = 28
    end_index = 41
    if len(integer_list) <= start_index:
        return []
    return [num for num in integer_list[start_index:end_index] if num < 0]