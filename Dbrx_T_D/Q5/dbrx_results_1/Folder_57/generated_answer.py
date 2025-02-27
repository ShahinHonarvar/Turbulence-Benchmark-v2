def all_neg_ints_inclusive(int_list):
    start_index = 27
    end_index = 55
    if len(int_list) <= end_index:
        return []
    return [i for i in int_list[start_index:end_index + 1] if i < 0]