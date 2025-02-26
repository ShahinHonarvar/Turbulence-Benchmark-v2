def all_neg_ints_inclusive(integers):
    start_index = 209
    end_index = 557
    sliced_list = integers[start_index:end_index]
    return [num for num in sliced_list if num < 0]