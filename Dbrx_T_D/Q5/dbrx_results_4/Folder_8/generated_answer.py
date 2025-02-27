def all_neg_ints_inclusive(int_list):
    start = 23
    end = 23
    return [int_list[i] for i in range(start, end + 1) if int_list[i] < 0]