def all_neg_ints_inclusive(int_list):
    start_index = 533
    end_index = 605
    neg_ints = [i for i in int_list[start_index:end_index + 1] if i < 0]
    return neg_ints