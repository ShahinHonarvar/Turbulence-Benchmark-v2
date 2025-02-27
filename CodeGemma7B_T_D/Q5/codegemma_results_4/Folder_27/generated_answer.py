def all_neg_ints_inclusive(l):
    if not any((i < 0 for i in l)):
        return []
    return [i for i in l[66:94] if i < 0]