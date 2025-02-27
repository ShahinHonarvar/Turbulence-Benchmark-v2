def all_neg_ints_exclusive(integer_list):
    start_index = 73
    end_index = 84
    negatives = [i for i in integer_list[start_index:end_index] if i < 0]
    return negatives