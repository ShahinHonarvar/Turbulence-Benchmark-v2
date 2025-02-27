def all_neg_ints_exclusive(list):
    if not any((i < 0 for i in list[44:78])):
        return []
    return [i for i in list[44:78] if i < 0]