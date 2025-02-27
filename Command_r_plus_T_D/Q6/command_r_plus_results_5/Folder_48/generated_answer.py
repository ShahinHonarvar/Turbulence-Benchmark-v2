def all_neg_ints_exclusive(int_list):
    start_index = 385
    end_index = 999
    neg_ints = [num for i, num in enumerate(int_list[start_index:end_index], start_index) if num < 0]
    return neg_ints