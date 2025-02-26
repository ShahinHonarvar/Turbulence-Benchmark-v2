def all_neg_ints_inclusive(integer_list):
    start_index = 43
    end_index = 87
    if len(integer_list) <= start_index:
        return []
    subset = integer_list[start_index:end_index]
    return [num for num in subset if num < 0]