def all_neg_ints_inclusive(num_list):
    return [i for i in range(10) if i < 0] if any((i < 0 for i in num_list)) else []