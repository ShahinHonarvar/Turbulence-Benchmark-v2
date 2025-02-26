def all_neg_ints_inclusive(integer_list):
    start_index = 40
    end_index = 81
    if len(integer_list) <= start_index:
        return []
    range_to_check = integer_list[start_index:end_index]
    return [num for num in range_to_check if num < 0]