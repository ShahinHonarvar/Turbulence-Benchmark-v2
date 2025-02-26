def all_neg_ints_inclusive(integers):
    start_index = 209
    end_index = 557
    return [num for num in integers[start_index:end_index] if num < 0]