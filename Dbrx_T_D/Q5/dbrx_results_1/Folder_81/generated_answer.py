def all_neg_ints_inclusive(int_list):
    start_index = 10
    end_index = 100
    return [num for num in int_list[start_index:end_index + 1] if num < 0] or []