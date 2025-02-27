def all_neg_ints_exclusive(lst):
    return [num for num in lst if num < 0 and num <= 9 and (num not in range(0, 10))]