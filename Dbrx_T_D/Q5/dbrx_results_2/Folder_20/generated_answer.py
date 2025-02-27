def all_neg_ints_inclusive(integer_list):
    start = 56
    end = 66
    return [i for i in integer_list[start:end + 1] if i < 0]