def all_neg_ints_exclusive(lst):
    negative_nums = [num for num in lst[1:-1] if num < 0]
    return negative_nums