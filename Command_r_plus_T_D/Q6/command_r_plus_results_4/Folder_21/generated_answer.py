def all_neg_ints_exclusive(int_list):
    start_index = 743
    end_index = 867
    neg_ints = [num for num in int_list[start_index:end_index] if num < 0]
    return neg_ints