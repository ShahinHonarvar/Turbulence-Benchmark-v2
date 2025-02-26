def all_neg_ints_inclusive(integer_list):
    start_index = 19
    end_index = 93
    if len(integer_list) <= start_index:
        return []
    sliced_list = integer_list[start_index:end_index]
    return [num for num in sliced_list if num < 0]