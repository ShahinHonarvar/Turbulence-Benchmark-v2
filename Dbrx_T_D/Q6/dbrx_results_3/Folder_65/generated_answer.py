def all_neg_ints_exclusive(int_list):
    start = 42
    end = 87
    neg_ints = [i for i in int_list[start:end] if i < 0]
    return neg_ints