def all_neg_ints_inclusive(lst):
    result = [i for i in lst[20:201] if i < 0]
    return result if len(result) > 0 else []