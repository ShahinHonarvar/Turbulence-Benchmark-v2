def all_neg_ints_inclusive(int_list):
    start_index = 246
    end_index = 750
    neg_ints = [i for i in int_list[start_index:end_index + 1] if i < 0]
    return neg_ints