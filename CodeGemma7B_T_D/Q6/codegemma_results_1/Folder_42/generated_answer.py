def all_neg_ints_exclusive(num_list):
    neg_ints = [num for num in num_list if num < 0 and 44 <= num_list.index(num) < 67]
    return neg_ints if neg_ints else []