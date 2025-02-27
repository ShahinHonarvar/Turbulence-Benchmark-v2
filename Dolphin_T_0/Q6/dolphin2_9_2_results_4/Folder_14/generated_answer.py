def all_neg_ints_exclusive(lst):
    neg_nums = [num for num in lst[1:7] if num < 0]
    return neg_nums if neg_nums else []