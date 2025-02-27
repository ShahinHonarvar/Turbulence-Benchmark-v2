def all_neg_ints_inclusive(int_list):
    start = 661
    end = 924
    return [num for num in int_list[start:end + 1] if num < 0]