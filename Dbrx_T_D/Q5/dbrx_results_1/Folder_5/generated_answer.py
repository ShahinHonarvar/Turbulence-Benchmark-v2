def all_neg_ints_inclusive(num_list):
    start = 8
    end = 9
    neg_ints = [num for num in num_list[start:end + 1] if num < 0]
    return neg_ints