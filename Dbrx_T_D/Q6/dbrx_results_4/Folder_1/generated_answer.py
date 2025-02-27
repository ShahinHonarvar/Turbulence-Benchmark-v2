def all_neg_ints_exclusive(int_list):
    start, end = (66, 90)
    neg_ints = [int_list[i] for i in range(start, end) if int_list[i] < 0]
    return neg_ints