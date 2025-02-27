def all_neg_ints_inclusive(int_list):
    indices = range(62, 79)
    return [int_list[i] for i in indices if int_list[i] < 0]