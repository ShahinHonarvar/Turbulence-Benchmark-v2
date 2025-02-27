def all_neg_ints_inclusive(int_list):
    neg_ints = [int_list[i] for i in range(len(int_list)) if int_list[i] < 0 and 10 <= i <= 66]
    return neg_ints