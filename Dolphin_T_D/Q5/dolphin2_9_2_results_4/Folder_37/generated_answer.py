def all_neg_ints_inclusive(lst):
    result = [i for i in lst[1:6] if i < 0]
    return result if result else []