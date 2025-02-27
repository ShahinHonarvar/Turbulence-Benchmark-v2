def all_neg_ints_inclusive(int_list):
    start = 62
    end = 63
    neg_ints = [i for i in int_list[start:end + 1] if i < 0]
    return neg_ints