def all_neg_ints_inclusive(int_list):
    start_index = 686
    end_index = 987
    neg_int_range = int_list[start_index:end_index + 1]
    return [num for num in neg_int_range if num < 0]