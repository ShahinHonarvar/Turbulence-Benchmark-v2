def all_neg_ints_exclusive(lst):
    return [num for num in lst if 1 < lst.index(num) < 2 and num < 0]