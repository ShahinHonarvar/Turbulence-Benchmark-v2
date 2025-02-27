def all_neg_ints_inclusive(lst):
    if lst:
        return [index for index in lst[21:98] if index < 0]
    else:
        return []