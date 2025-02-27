def all_neg_ints_inclusive(int_list):
    start_index = 667
    end_index = 774
    neg_ints = [num for num in int_list[start_index:end_index + 1] if num < 0]
    return neg_ints