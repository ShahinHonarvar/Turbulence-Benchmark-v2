def all_neg_ints_exclusive(integer_list):
    start = 44
    end = 91
    neg_ints = [i for i in integer_list[start:end] if i < 0]
    return neg_ints