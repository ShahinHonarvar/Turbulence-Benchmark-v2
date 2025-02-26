def all_neg_ints_inclusive(integer_list):
    start_index = 59
    end_index = 98
    if len(integer_list) <= start_index:
        return []
    sublist = integer_list[start_index:end_index]
    return [num for num in sublist if num < 0]