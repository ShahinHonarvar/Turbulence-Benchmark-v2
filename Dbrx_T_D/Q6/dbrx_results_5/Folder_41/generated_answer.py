def all_neg_ints_exclusive(integer_list):
    start = 8
    end = 10
    neg_ints = [i for i in integer_list[start:end] if i < 0]
    return neg_ints