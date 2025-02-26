def all_neg_ints_inclusive(integer_list):
    start_index = 36
    end_index = 47
    if len(integer_list) < end_index:
        end_index = len(integer_list)
    return [num for num in integer_list[start_index:end_index] if num < 0]