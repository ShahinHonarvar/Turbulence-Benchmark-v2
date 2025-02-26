def all_neg_ints_inclusive(int_list):
    start = min(62, len(int_list))
    end = min(93, len(int_list))
    return [num for num in int_list[start:end] if num < 0]