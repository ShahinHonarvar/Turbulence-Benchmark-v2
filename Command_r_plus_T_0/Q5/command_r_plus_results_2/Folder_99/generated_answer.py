def all_neg_ints_inclusive(int_list):
    start_index = 310
    end_index = 370
    neg_ints = [num for num in int_list[start_index:end_index + 1] if num < 0]
    return neg_ints