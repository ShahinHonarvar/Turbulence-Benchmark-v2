def all_neg_ints_exclusive(int_list):
    portion = int_list[599:767]
    negatives = [x for x in portion if x < 0]
    return negatives