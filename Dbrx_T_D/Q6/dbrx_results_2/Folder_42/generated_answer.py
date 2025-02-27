def all_neg_ints_exclusive(int_list):
    start = 44
    end = 67
    neg_ints = [i for i in int_list[start:end] if i < 0]
    return neg_ints