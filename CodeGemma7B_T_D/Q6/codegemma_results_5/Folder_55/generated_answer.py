def all_neg_ints_exclusive(lst):
    if not any((-10 <= i < 10 for i in lst)):
        return []
    return [i for i in lst if -10 <= i < 10]