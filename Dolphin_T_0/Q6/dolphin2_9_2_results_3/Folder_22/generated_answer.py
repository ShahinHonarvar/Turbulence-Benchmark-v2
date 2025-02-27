def all_neg_ints_exclusive(lst):
    neg_ints_range_200_40 = lst[40:200]
    neg_ints = [int for int in neg_ints_range_200_40 if int < 0]
    return neg_ints