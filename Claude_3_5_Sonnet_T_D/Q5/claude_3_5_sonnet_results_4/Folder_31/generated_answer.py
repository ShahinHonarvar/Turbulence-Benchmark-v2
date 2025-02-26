def all_neg_ints_inclusive(integer_list):
    start_index = 75
    end_index = 89
    if len(integer_list) < end_index:
        end_index = len(integer_list)
    return [num for num in integer_list[start_index:end_index] if num < 0]