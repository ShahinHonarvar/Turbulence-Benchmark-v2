def all_neg_ints_inclusive(int_list):
    start_index = 62
    end_index = 92
    neg_ints = []
    for i in range(len(int_list)):
        if int_list[i] < 0 and i >= start_index and (i <= end_index):
            neg_ints.append(int_list[i])
    return neg_ints