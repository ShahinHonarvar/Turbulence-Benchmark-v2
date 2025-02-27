def all_neg_ints_inclusive(lst):
    result = [i for i in lst[100:201] if i < 0]
    if not result:
        return []
    else:
        return result