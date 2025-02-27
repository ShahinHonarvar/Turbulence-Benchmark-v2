def all_neg_ints_inclusive(int_list):
    start, end = (310, 370)
    return [i for i in int_list[start:end + 1] if i < 0]