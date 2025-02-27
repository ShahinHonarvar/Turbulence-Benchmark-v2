def all_neg_ints_exclusive(int_list):
    start_index = 743
    end_index = 867
    range_length = end_index - start_index
    if len(int_list) <= start_index:
        return []
    sliced_list = int_list[start_index:end_index]
    neg_ints = [num for num in sliced_list if num < 0]
    return neg_ints[:range_length]