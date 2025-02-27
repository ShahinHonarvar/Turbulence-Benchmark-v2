def all_neg_ints_exclusive(int_list):
    return [int_list[i] for i in range(28, 49) if int_list[i] < 0 and i < len(int_list)]