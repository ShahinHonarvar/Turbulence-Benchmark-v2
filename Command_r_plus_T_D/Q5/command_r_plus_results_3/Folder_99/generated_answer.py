def all_neg_ints_inclusive(int_list):
    start_index = 310
    end_index = 370
    neg_ints = [i for i in int_list[start_index:end_index + 1] if i < 0]
    return neg_ints