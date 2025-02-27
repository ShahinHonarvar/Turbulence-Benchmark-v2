def all_neg_ints_inclusive(int_list):
    start_index = 75
    end_index = 85
    neg_int_range = int_list[start_index:end_index + 1]
    return [i for i in neg_int_range if i < 0]