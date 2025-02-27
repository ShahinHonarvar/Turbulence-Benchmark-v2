def all_neg_ints_exclusive(int_list):
    return [neg for i, neg in enumerate(int_list[1:7]) if neg < 0]